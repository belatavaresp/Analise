Dadas $\sum a_n$ e $\sum b_n$ tais que $a_n \geq 0, b_n \geq 0 \ \forall n\geq1$ e tais que existe $M>0$ e $a_n \leq M \cdot b_n, n\geq 1$.

1. $\sum b_n < +\infty \Rightarrow \sum a_n < +\infty$, ou seja, se a série dos $b_n$ converge, então a série dos $a_n$ também.
2. $\sum a_n = +\infty \Rightarrow \sum b_n = +\infty$, ou seja se a série dos $a_n$ diverge, então a série dos $b_n$ também.
### Demonstração:
Sejam $s_n = a_1+...+a_n, \ t_n = b_1+...+b_n$:
1. Seja $t_n \leq k \ \forall n \in \mathbb{N} \Rightarrow s_n\leq M\cdot k \ \forall n \in \mathbb{N} \Rightarrow (s_n)$ converge.
2. $\sum a_n = +\infty \iff s_n \to +\infty$, como $s_n \leq M \cdot t_n \Rightarrow t_n \geq \frac{1}{M}s_n \Rightarrow t_n \to +\infty \Rightarrow \sum b_n = +\infty$