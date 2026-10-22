# 正交多项式部分和单一阈值猜想的反例

**作者：Aurantium。** [English](README.md) · [完整证明](counterexample.md) · [参考文献](REFERENCES.md) · [复现说明](REPRODUCIBILITY.md)

同一个三次部分和在 $t=1/3$ 时有三个实单根，却在更大的 $t=1/2$ 时出现一对非实共轭根。这否定了 **arXiv:2409.00261v2 所述的一般情形 Conjecture 3.4**。构造来自真正的无限正交多项式族，正交测度为紧支撑正概率测度。

## 原题与研究沿革

Erik Koelink、Pablo Román、Wadim Zudilin 在 *A partial-sum deformation for a family of orthogonal polynomials* 中提出猜想。论文于 **2024 年 8 月 30 日首次提交**，已核对的 v2 日期为 **2025 年 2 月 7 日**。书目记录给出期刊出处 **Indagationes Mathematicae 36（2025），第 6 期，1745–1761 页**，DOI：[10.1016/j.indag.2025.04.007](https://doi.org/10.1016/j.indag.2025.04.007)。**本次未能取得期刊最终全文，不能声称其表述已核实与 arXiv v2 完全一致。**

原文 Proposition 3.1 已证明：当正参数 $t$ 足够大时，部分和具有实单根并交错。Conjecture 3.4 进一步预测，存在唯一的正阈值，使阈值以上全为实单根、阈值以下总有非实共轭根。论文还研究 Hermite、Charlier、Lommel 例子。Antonio J. Durán 的两篇 2025 年相关论文处理不同的归一化或次数量词，不等于这个一般的固定次数阈值断言。详细出处见[参考文献](REFERENCES.md)。

## 精确反例与额外现象

取 $p_{-1}=0$、$p_0=1$，递推为

$$
p_{n+1}(x)=(x-b_n)p_n(x)-c_np_{n-1}(x),\qquad
b_2=-2,\quad b_n=0\ (n\ne2),\quad c_1=9,\quad c_n=1\ (n\ge2).
$$

部分和系数全部取 $\alpha_n=1$。有界 Jacobi 算子给出支撑包含于 $[-4,4]$、具有无限支撑的正概率正交测度。相应部分和为

$$
q_3(x;t)=1+tx+t^2(x^2-9)+t^3(x^3+2x^2-10x-18).
$$

- $27q_3(x;1/3)=x^3+5x^2-x-18$ 在 $(-5,-4)$、$(-3,-2)$、$(1,2)$ 内各有一根。
- $8q_3(x;1/2)=x^3+4x^2-6x-28$ 的判别式为 $-464$，因此有一个实根和一对非实共轭根。

由此不存在满足原猜想的正阈值。更强的现象是：在 $t=1/4,1/3,1/2,1$ 处，实根数依次为 **1、3、1、3**。这些性质在相应开邻域内保持，不是孤立重根导致的边界现象。

## 范围与验证等级

本项目否定的是一般的 arXiv v2 命题，不否定 Proposition 3.1，也不解决 Hermite、Charlier、Lommel 特定归一化下的独立问题。原题始于 2024 年，不是 Zudilin 在 2015 年提出的 B 多项式问题；这里不声称给出更广的分类或替代阈值定理。

[通常数学证明](counterexample.md)已通过[另一次 AI 数学审查](independent_review.md)。精确符号计算及仅使用标准库有理数的 Sturm 检查器可以复现有限证书。**不声称经过独立人类同行评审，也不声称完成全 Lean 或其他证明助手认证。** 有限检索未找到此前解答，但不保证新颖性或全球优先权。

使用 Python 3.10 及以上版本和 `requirements.txt` 中记录的依赖版本，不使用 `-O`：

```sh
python verify_counterexample.py
python verify_sturm_fraction.py
python check_package.py
```

最后一项仅检查文件完整性。精确范围、日志、文件及哈希见[复现说明](REPRODUCIBILITY.md)、[PUBLIC_FILES.txt](PUBLIC_FILES.txt)与[SHA256SUMS.json](SHA256SUMS.json)。AI 辅助、原有成果归属和复用状态见[RIGHTS.md](RIGHTS.md)。
