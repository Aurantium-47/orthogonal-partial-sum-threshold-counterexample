# A counterexample to the orthogonal partial-sum threshold conjecture

**Author: Aurantium.** [中文](README.zh.md) · [Proof](counterexample.md) · [Sources](REFERENCES.md) · [Verification](REPRODUCIBILITY.md)

A cubic partial sum has three simple real roots at $t=1/3$, but a nonreal conjugate pair at the larger value $t=1/2$. This disproves **Conjecture 3.4 as stated in arXiv:2409.00261v2**, for a genuine infinite orthogonal polynomial system with a positive compactly supported probability measure.

## Origin and previous work

Erik Koelink, Pablo Román, and Wadim Zudilin introduced the conjecture in *A partial-sum deformation for a family of orthogonal polynomials*, first submitted on **30 August 2024**; the inspected v2 is dated **7 February 2025**. The bibliographic record identifies **Indagationes Mathematicae 36 (2025), no. 6, 1745–1761**, DOI [10.1016/j.indag.2025.04.007](https://doi.org/10.1016/j.indag.2025.04.007). **The final journal full text was inaccessible; identical journal wording has not been verified.**

Their Proposition 3.1 proves real simple roots and interlacing for sufficiently large positive $t$. Conjecture 3.4 further predicts a single positive threshold separating that behavior from a nonreal pair for every smaller positive $t$. The paper also studies Hermite, Charlier, and Lommel examples. Antonio J. Durán's related 2025 papers study different normalizations and/or degree quantifiers, not this general fixed-degree threshold. See [REFERENCES.md](REFERENCES.md).

## Exact construction and contradiction

Set $p_{-1}=0$, $p_0=1$, and

$$
p_{n+1}(x)=(x-b_n)p_n(x)-c_np_{n-1}(x),\qquad
b_2=-2,\quad b_n=0\ (n\ne2),\quad c_1=9,\quad c_n=1\ (n\ge2).
$$

All partial-sum coefficients are $\alpha_n=1$. The bounded Jacobi operator supplies a positive probability orthogonality measure supported in $[-4,4]$ with infinite support. For

$$
q_3(x;t)=1+tx+t^2(x^2-9)+t^3(x^3+2x^2-10x-18),
$$

- $27q_3(x;1/3)=x^3+5x^2-x-18$ has one root in each of $(-5,-4)$, $(-3,-2)$, and $(1,2)$.
- $8q_3(x;1/2)=x^3+4x^2-6x-28$ has discriminant $-464$, hence one real root and a nonreal conjugate pair.

No positive threshold can satisfy the conjecture. More strongly, the exact root counts at $t=1/4,1/3,1/2,1$ are respectively **1, 3, 1, 3**; this reentrant behavior persists on open neighborhoods, so it is not an isolated multiple-root effect.

## Scope and validation

The construction refutes the general arXiv v2 statement; it does not refute Proposition 3.1 or settle the separately normalized Hermite, Charlier, or Lommel cases. It is a 2024-origin question, distinct from Zudilin's 2015 B-polynomial observation. No broader classification or replacement threshold theorem is claimed.

The [ordinary proof](counterexample.md) passed a [separate AI mathematical audit](independent_review.md). Exact symbolic calculations and a standard-library rational Sturm checker reproduce the finite certificates. **Neither independent human peer review nor full Lean/proof-assistant certification is claimed.** The bounded literature search found no earlier resolution, but novelty and priority remain uncertified.

Use Python 3.10 or newer and the dependency in `requirements.txt`, without `-O`:

```sh
python verify_counterexample.py
python verify_sturm_fraction.py
python check_package.py
```

The last command checks file integrity only. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md), [PUBLIC_FILES.txt](PUBLIC_FILES.txt), and [SHA256SUMS.json](SHA256SUMS.json). AI assistance, source attribution, and reuse status are disclosed in [RIGHTS.md](RIGHTS.md).
