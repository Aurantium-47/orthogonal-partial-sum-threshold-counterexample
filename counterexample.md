# Reentrant real-rootedness disproves the general partial-sum threshold conjecture

**Author: Aurantium.** Version dated 22 October 2026. The written proof passed a separate AI mathematical audit, not independent human peer review. The verified target is arXiv v2; no full Lean certification or novelty guarantee is claimed.

## Target and exact scope

The mathematical target verified here is Conjecture 3.4 in arXiv:2409.00261v2. The final journal text has not been compared, so this note does not assert that the published journal version contains the same conjecture.

Erik Koelink, Pablo Román, Wadim Zudilin, *A partial-sum deformation for a family of orthogonal polynomials*, arXiv:2409.00261, originally submitted 30 August 2024; latest listed version v2, 7 February 2025; Indagationes Mathematicae 36 (2025), no. 6, 1745–1761; DOI 10.1016/j.indag.2025.04.007.

Primary full text: https://arxiv.org/html/2409.00261v2 . Bibliographic/version record: https://arxiv.org/abs/2409.00261 .

The following is a mathematical restatement, rather than a verbatim quotation, of Conjecture 3.4 in arXiv:2409.00261v2, with all preceding hypotheses. Let

    x p_n = a_n p_{n+1} + b_n p_n + c_n p_{n-1},
    p_{-1}=0, p_0=1, a_n !=0, a_{n-1}c_n>0,
    alpha_0=1, alpha_n real and nonzero,
    q_N(x;t)=sum_{n=0}^N alpha_n t^n p_n(x).

For every N>0 the conjecture asserts the existence of T=T(N)>0 such that:

* for every t>T, q_N as a polynomial in x has N distinct real zeros;
* for every 0<t<T, q_N has a nonreal conjugate pair of zeros.

These are the conditions in the arXiv v2 text, Section 2, the opening of Section 3, and Conjecture 3.4. In particular, the general claim is not restricted to the three classical examples of Section 4. Our counterexample has N=3, all a_n=1 (monic normalization), all alpha_n=1, strictly positive c_n, and a compactly supported positive probability orthogonality measure. It does not exploit the degree-one oversight or a zero coefficient, degenerate measure, negative normalization, or isolated multiple root.

## Construction of a valid infinite orthogonal family

Take

    b_2=-2, b_n=0 for n!=2,
    c_1=9, c_n=1 for every n>=2,
    a_n=1 for all n>=0, alpha_n=1 for all n>=0.

Define p_{-1}=0, p_0=1 and recursively

    p_{n+1}(x)=(x-b_n)p_n(x)-c_n p_{n-1}(x).

(The value of c_0 is irrelevant.) Inductively every p_n is monic of degree n. Every Favard product a_{n-1}c_n is strictly positive, so Favard's theorem supplies a positive probability measure of infinite support for which the p_n are orthogonal.

For an explicit operator justification of the compactness and nondegeneracy assertions, let J act on ell^2(N_0) with diagonal b_n and off-diagonal entries d_1=3,d_n=1 for n>=2. Thus J e_n=d_n e_{n-1}+b_n e_n+d_{n+1}e_{n+1}, with the nonexistent first summand omitted for n=0. Every absolute row sum of J is at most 4, so J is a bounded self-adjoint real Jacobi operator of norm at most 4. Its spectral measure at the unit vector e_0 is a positive probability measure supported on [-4,4]. The recurrence gives

    p_0(J)e_0=e_0,
    p_n(J)e_0=(d_1...d_n)e_n=3e_n  (n>=1).

Therefore the integral of p_m p_n against this measure is zero for m!=n and strictly positive for m=n. The squared norms are h_0=1 and h_n=9 for n>=1. An infinite orthogonal set of nonzero vectors rules out finite support. This verifies all measure assumptions independently of any formal extension of a finite polynomial list.

The first polynomials are

    p_0=1,
    p_1=x,
    p_2=x^2-9,
    p_3=x^3+2x^2-10x-18.

Consequently

    q_3(x;t)=1+tx+t^2(x^2-9)+t^3(x^3+2x^2-10x-18).

## Exact contradiction

At t=1/3,

    27q_3(x;1/3)=P(x)=x^3+5x^2-x-18.

The values

    P(-5)=-13, P(-4)=2,
    P(-3)=3,   P(-2)=-4,
    P(1)=-13,  P(2)=8

give one real zero in each of the three disjoint intervals (-5,-4), (-3,-2), (1,2). A cubic has at most three roots, so these are precisely three distinct simple real roots.

At the larger parameter t=1/2,

    8q_3(x;1/2)=R(x)=x^3+4x^2-6x-28.

For a monic cubic x^3+Ax^2+Bx+C the discriminant is

    Delta=A^2 B^2-4B^3-4A^3 C-27C^2+18ABC.

For R, this gives

    Delta=576+864+7168-21168+12096=-464<0.

A real cubic of negative discriminant has exactly one real root and one nonreal conjugate pair. For completeness: a nonzero discriminant excludes repeated roots; if all three roots were real, the discriminant product of squared pairwise differences would be positive. Every real odd-degree polynomial has a real root; hence the remaining two must be nonreal and conjugate.

There can be no conjectured threshold T. If T<=1/3, the nonreal pair at 1/2>T contradicts the first requirement. If T>1/3, the three real roots at 1/3<T contradict the second requirement. This covers every T>0, including equality T=1/3 or 1/2.

Thus Conjecture 3.4 as stated in arXiv:2409.00261v2 is false in its generality.

## Stronger reentrant behavior and reproducible certificate

The discriminant of q_3 is exactly

    disc_x(q_3)=t^6 D(t),
    D(t)=2708t^6-716t^5-1531t^4+140t^3+236t^2+16t-16.

The exact values

    D(1/4)=-1107/1024,
    D(1/3)=1901/729,
    D(1/2)=-29/4,
    D(1)=837

show the sequence: one real root, three real roots, one real root, three real roots as t increases over 1/4, 1/3, 1/2, 1. Strict inequalities persist on open neighborhoods, so this is genuine reentrant behavior, not a boundary coincidence. The necessary disproof uses only 1/3 and 1/2.

The companion script verify_counterexample.py uses exact SymPy rational arithmetic, verifies the recurrence, all displayed evaluations and discriminants, and exact Sturm counts. No floating-point root computation is needed for the proof.

## Status and limitations

This resolves the general statement negatively; it does not refute any separate claim restricted to Hermite, Charlier, or Lommel families with their specific normalizations. Nor is it a result from 2015: the present target dates to 2024 and is distinct from Zudilin's 2015 B-polynomial zero-location observation.

The bibliographic record identifies a 2025 journal publication, but the publisher's final full text was inaccessible in this review. The result therefore targets the independently inspected arXiv v2 text, not a verified identical journal statement. The HTML's internally generated date is inconsistent with the arXiv version history; chronology here follows the version record.

The original Proposition 3.1 proves real, simple roots for sufficiently large positive t. The counterexample is compatible with that result: it refutes a single-threshold description of the entire positive parameter axis, not eventual real-rootedness.

Antonio J. Durán's 2025 papers on zeros of linear combinations of orthogonal polynomials and of Hermite polynomials study different normalizations and/or different quantifiers; they do not supply the fixed-degree, fixed-normalization threshold asserted here. See [REFERENCES.md](REFERENCES.md) and [literature_status.md](literature_status.md).

Targeted searches found no earlier resolution of this precise statement. This bounded search does not certify priority. No independent human peer review, author endorsement, or full proof-assistant certification is claimed. See [independent_review.md](independent_review.md) for the audit and [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for the exact checks.
