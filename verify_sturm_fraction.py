#!/usr/bin/env python3
"""Reproduce the two rational Sturm certificates using only Python's stdlib.

This release checker reconstructs the chains printed in the separate AI audit.
It is independent of SymPy, but is not a proof-assistant or human certification.
Coefficients below are ordered from constant term to leading term.
"""
from fractions import Fraction as F

if not __debug__:
    raise RuntimeError("Run verification without Python -O; assertions must be enabled.")

def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p

def derivative(p):
    return [i * p[i] for i in range(1, len(p))]

def remainder(p, q):
    p, q = trim(p), trim(q)
    if not q:
        raise ZeroDivisionError("Zero polynomial divisor")
    while p and len(p) >= len(q):
        shift = len(p) - len(q)
        factor = p[-1] / q[-1]
        for i, coefficient in enumerate(q):
            p[i + shift] -= factor * coefficient
        p = trim(p)
    return p

def sturm(p):
    chain = [list(map(F, p)), derivative(list(map(F, p)))]
    while chain[-1]:
        r = [-v for v in remainder(chain[-2], chain[-1])]
        if not r:
            break
        chain.append(r)
    return chain

def infinity_sign(p, negative):
    lead_sign = 1 if p[-1] > 0 else -1
    return lead_sign * (-1 if negative and (len(p)-1) % 2 else 1)

def variations(signs):
    return sum(a != b for a, b in zip(signs, signs[1:]))

certificates = [
    ("P", [-18, -1, 5, 1],
     [[-18, -1, 5, 1], [-1, 10, 3], [F(157,9), F(56,9)], [F(17109,3136)]], 3, 0),
    ("R", [-28, -6, 4, 1],
     [[-28, -6, 4, 1], [-6, 8, 3], [F(228,9), F(68,9)], [F(-261,289)]], 2, 1),
]
for name, p, expected, left, right in certificates:
    chain = sturm(p)
    assert chain == expected
    assert len(chain[-1]) == 1 and chain[-1][0] != 0
    vleft = variations([infinity_sign(q, True) for q in chain])
    vright = variations([infinity_sign(q, False) for q in chain])
    assert (vleft, vright) == (left, right)
    print(f"{name}: exact Sturm chain = " + str([[str(v) for v in q] for q in chain]))
    print(f"{name}: V(-infinity)={vleft}; V(+infinity)={vright}; distinct real roots={vleft-vright}")
print("PASS: both exact rational Sturm certificates and squarefreeness")
