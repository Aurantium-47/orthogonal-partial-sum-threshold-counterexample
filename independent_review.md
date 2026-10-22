# Independent AI review of the KRZ counterexample

Review date: 22 October 2026.

This publication-edited report records a separate AI audit. It is not independent human peer review. Mathematical findings and verification limits are preserved; editorial workflow details are omitted.

## Verdict

**Mathematical validity: PASS.** The construction disproves Conjecture 3.4 as stated in arXiv:2409.00261v2, with a genuine infinite orthogonal polynomial system for a positive compactly supported probability measure. The contradiction is not attributable to normalization, sign-changing coefficients, a finite family, the degree-one exception, or a parameter-domain mismatch.

**Novelty/priority: NOT CERTIFIED.** Targeted searches and inspection of relevant subsequent papers found no resolution of this precise threshold conjecture. That negative search result is not evidence sufficient to claim priority. The final publisher full text was not accessible in this review, so the verdict is explicitly against the verified arXiv v2 statement.

## 1. Original statement and quantifiers

The audit independently inspected https://arxiv.org/html/2409.00261v2 and https://arxiv.org/abs/2409.00261. The submission dates are 30 August 2024 and 7 February 2025 (v2).

Section 2 allows a real three-term recurrence with p_{-1}=0, p_0=1, nonzero leading recurrence coefficients, and nonzero real alpha_n with alpha_0=1; monic normalization is permitted. Section 3 adds a_{n-1}c_n>0. Conjecture 3.4 requires one positive threshold at each fixed degree: all zeros real and simple above it, a nonreal pair below it. No classical-family, orthonormality, or generating-series-convergence restriction appears.

The proposed a_n=alpha_n=1 and strictly positive c_n satisfy these hypotheses. Both tested parameters are positive. The conjecture does not require all real zeros to remain in the measure's convex hull, so the q_3 root below -4 is not a disqualification.

## 2. Infinite orthogonality and positive measure

The supplied infinite Jacobi-operator argument is correct. On ell^2(N_0), the real symmetric tridiagonal matrix with diagonal b_2=-2, b_n=0 otherwise, and off-diagonal d_1=3, d_n=1 for n>=2 defines a bounded self-adjoint operator. A concrete additional bound is ||J||<=4: every absolute row sum and column sum is at most 4, so the Schur bound applies.

The spectral measure mu of J at the unit vector e_0 is consequently a positive probability measure supported in [-4,4]. Induction using c_n=d_n^2 gives p_n(J)e_0=(d_1...d_n)e_n. Thus p_0(J)e_0=e_0 and p_n(J)e_0=3e_n for every n>=1. Functional calculus then yields integral p_m p_n dmu=0 for m!=n, with squared norms 1 for n=0 and 9 for n>=1. These strictly positive norms and infinitely many orthogonal functions exclude finite support. Compact support also guarantees all moments exist.

The argument does not need an explicit density, an assertion that the measure is atomless, or an assumption that the support is a single interval. None of those is required by the verified target statement.

## 3. Polynomial calculations and threshold contradiction

Independent expansion confirms p_1=x, p_2=x^2-9 and p_3=x^3+2x^2-10x-18. At t=1/3, the scaled partial sum is P=x^3+5x^2-x-18. Its values at -5,-4,-3,-2,1,2 are -13,2,3,-4,-13,8. The intermediate value theorem gives three distinct zeros in the disjoint intervals (-5,-4), (-3,-2), (1,2). Because its degree is three, every zero is simple and real.

At t=1/2, the scaled partial sum is R=x^3+4x^2-6x-28. Its discriminant is -464. A real cubic with negative discriminant has one real root and a nonreal conjugate pair, with no repeated roots.

The threshold case split is exhaustive. If T<=1/3, then 1/2>T contradicts the claimed all-real region. If T>1/3, then 1/3<T contradicts the claimed nonreal-pair region. Equality cases cause no loophole.

The audit reran verify_counterexample.py successfully and also checked the two relevant root counts using a separate exact rational Euclidean-algorithm implementation, with Python's fractions.Fraction and no SymPy:

- P Sturm chain: P, 3x^2+10x-1, (56x+157)/9, 17109/3136. Sign variations are 3 at -infinity and 0 at +infinity, hence three real roots.
- R Sturm chain: R, 3x^2+8x-6, (68x+228)/9, -261/289. Sign variations are 2 at -infinity and 1 at +infinity, hence one real root.

The manuscript's degree-six discriminant polynomial and its four rational sample values also passed the exact supplied script. Those values establish reentrant real-rootedness on open intervals, not just isolated multiple-root boundaries.

## 4. Verification scope

The supplied script is an exact symbolic/rational verification, not a Lean proof. Its successful execution verifies its algebraic identities, root counts, and squarefreeness assertions. It does not machine-verify the infinite-dimensional spectral theorem, the existence of the orthogonality measure, or the interpretation of the paper's conjecture. The written mathematical proof supplies those links. This release includes no compiled Lean artifact; these SymPy checks are not proof-assistant verification.

## 5. Literature comparison and limits

Two subsequent primary papers were compared:

1. Antonio J. Durán, Zeros of linear combinations of orthogonal polynomials, arXiv:2505.11956 (17 May 2025), https://arxiv.org/html/2505.11956v1. It studies a fixed-length combination of consecutive polynomials as the degree varies and proves eventual real-rootedness after a suitable normalization. It cites KRZ. These quantifiers do not provide monotonic real-rootedness in t for a fixed degree and a fixed normalization, so the theorem does not resolve or obstruct the counterexample.
2. Antonio J. Durán, Zeros of linear combinations of Hermite polynomials, arXiv:2505.15330 (21 May 2025), https://arxiv.org/html/2505.15330v1. It treats two Hermite normalizations and relates zeros of their finite combinations to a coefficient polynomial. It cites KRZ, but does not supply a general positive-t threshold theorem for arbitrary orthogonal families. The present counterexample is not a claim against the special Hermite assertions.

Additional searches used the target title, arXiv identifier, author names, Conjecture 3.4, threshold, counterexample, correction, and erratum. They returned no earlier resolution of this exact statement. That is a bounded search result, not a priority determination.

The publisher landing page is https://www.sciencedirect.com/science/article/pii/S0019357725000436. Direct full-text retrieval returned HTTP 403. A CONICET published-version record was located, but its full text was not retrievable through the available route. Therefore final-journal wording remains an explicit verification gap, rather than being silently treated as identical to arXiv v2. No author endorsement is claimed.

## Release consistency

The manuscript includes the explicit norm and support bound, the squared norms, the different-quantifier comparison with the Durán papers, and the publisher-text caveat. The exact supplied verifier was rerun after packaging. A separate standard-library rational Sturm checker was reconstructed from the audit's displayed chains and included for reproducibility; it is an additional computational check, not an independent human review or formal proof. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

No mathematical correction to the counterexample was required by this audit.
