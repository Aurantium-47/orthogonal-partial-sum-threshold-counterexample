#!/usr/bin/env python3
"""Exact symbolic verification of the cubic counterexample.
Run: python verify_counterexample.py. Requires SymPy; no external input or network.
"""
if not __debug__:
    raise RuntimeError("Run verification without Python -O; assertions must be enabled.")
import sympy as s
x,t=s.symbols('x t')
p=[s.Integer(1),x]
for n in range(1,8):
    b=-2 if n==2 else 0
    c=9 if n==1 else 1
    p.append(s.expand((x-b)*p[n]-c*p[n-1]))
assert p[2]==x*x-9 and p[3]==x**3+2*x*x-10*x-18
q=s.expand(sum(t**n*p[n] for n in range(4)))
D=2708*t**6-716*t**5-1531*t**4+140*t**3+236*t**2+16*t-16
assert s.expand(s.discriminant(q,x)-t**6*D)==0
P=s.expand(27*q.subs(t,s.Rational(1,3)))
R=s.expand(8*q.subs(t,s.Rational(1,2)))
assert [P.subs(x,v) for v in [-5,-4,-3,-2,1,2]]==[-13,2,3,-4,-13,8]
assert s.discriminant(P,x)==1901 and s.discriminant(R,x)==-464
for v,count,expected in [(s.Rational(1,4),1,-s.Rational(1107,1024)),(s.Rational(1,3),3,s.Rational(1901,729)),(s.Rational(1,2),1,-s.Rational(29,4)),(s.Integer(1),3,s.Integer(837))]:
    poly=s.Poly(q.subs(t,v),x)
    assert D.subs(t,v)==expected
    assert poly.count_roots(-s.oo,s.oo)==count
    assert s.gcd(poly,poly.diff()).degree()==0
    print('t=',v,' D(t)=',expected,' distinct real roots=',count)
print('PASS: all exact identities, sign certificates, and Sturm counts')
