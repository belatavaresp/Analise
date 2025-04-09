Seja $x_n$ uma [[Sequência]] que converge para o [[Limite]] $l$ e $z_n$ outra [[Sequência]] que converge para $l$. Se $y_n$ é uma [[Sequência]] tal que $x_n\leq y_n \leq z_n$ a partir de um $n \geq N\in \mathbb{N}$ então $y_n \to l$.
### Demonstração:
Seja $\epsilon > 0$ e sejam $N_1, N_2 \in \mathbb{N}$ tais que se temos $n\geq N_1 \Rightarrow l-\epsilon < x_n < l+\epsilon$ e se temos $n\geq N_2 \Rightarrow l-\epsilon < z_n < l+\epsilon$. Seja $\tilde{N} = max\{N_1, N_2, N\}$ então se temos $n\geq \tilde{N}$ então $l-\epsilon < x_n \leq y_n \leq z_n < l+\epsilon$ e portanto $l-\epsilon < y_n < l+\epsilon$ o que implica $y_n \to l$. $\Box$.

### Exemplo:
$x_n = 0$, $y_n = \frac{1}{n^2}$ e $z_n = \frac{1}{n} \Rightarrow 0 \leq \frac{1}{n^2} \leq \frac{1}{n} \Rightarrow \frac{1}{n^2} \to 0$. 