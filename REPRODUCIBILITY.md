# Reproducibility and verification scope

## Environment and commands

The packaged scripts were executed with Python 3.12.14 and SymPy 1.14.0 on 22 October 2026. Python 3.10 or newer is recommended. `requirements.txt` records the tested external dependency. The rational Sturm checker uses only the Python standard library. No network, account, external data file, or downloaded source paper is needed.

Run from the repository root with dependencies already available, without `-O`; the scripts reject optimized mode because assertions must remain enabled.

```sh
python verify_counterexample.py
python verify_sturm_fraction.py
```

## Exactly what is checked

- `verify_counterexample.py` constructs the beginning of the recurrence exactly, checks p_2 and p_3, expands q_3, and proves by symbolic identity that its discriminant is t^6 times the displayed degree-six polynomial. It verifies the six interval-endpoint evaluations, discriminants 1901 and -464 of the two scaled cubics, all four rational discriminant evaluations, exact real-root counts 1,3,1,3 at t=1/4,1/3,1/2,1, and squarefreeness at those parameters.
- `verify_sturm_fraction.py` independently of SymPy reconstructs the rational Euclidean-algorithm Sturm chains printed in the AI audit. It checks the complete chain coefficients and nonzero terminal constants, then verifies sign-variation differences 3-0=3 for P and 2-1=1 for R. This checker was added during release preparation to make the audit's separate rational calculation reproducible; it is not an additional independent human review.

Both packaged commands completed successfully. Their exact stdout appears in `logs/symbolic.txt` and `logs/sturm_fraction.txt`. The original symbolic checker had already been rerun successfully during the separate AI audit; its mathematical assertions were retained in this release.

## Limits

These exact finite certificates support the cubic contradiction without floating-point root finding. They do not machine-verify the infinite-dimensional spectral theorem, the orthogonality measure, or the interpretation of the source's hypotheses. Those parts are supplied by the written proof and discussed in the AI audit. No full Lean or other proof-assistant certification is included or claimed; no independent human peer review is claimed. The verified conjecture is the arXiv v2 text, not a confirmed identical journal version.

## File integrity

```sh
python check_package.py
```

`PUBLIC_FILES.txt` lists the exact release files, including `SHA256SUMS.json`. The latter stores SHA-256 hashes and byte sizes for every other listed file; it excludes its own hash to avoid circularity. Hash checking establishes file identity, not mathematical correctness, source priority, or review status. Third-party full papers, scratch files, and caches are excluded from the release list.
