### Definição:
Uma [[Série numérica]] convergente $\sum a_n$ se chama comutativamente convergente se para toda bijeção $\phi: \mathbb{N} \to \mathbb{N}$ vale que $\sum a_{\phi(n)}$ converge e $\sum a_n = \sum a_{\phi(n)}$.

Ou seja defina $b_n = a_{\phi(n)}$ então:

1. $\sum b_n$ converge
2. $\sum b_n = \sum a_n$

### Teorema 1:
Se $\sum a_n$ é [[Série absolutamente convergente]] então $\sum a_n$ é comutativamente convergente.
#### Demonstração:
Seja $\phi: \mathbb{N} \to \mathbb{N}$ uma bijeção.
##### Parte 1, $a_n \geq 0, \ \forall n \in \mathbb{N}$:
$s_n = a_1+...+a_n$
$t_n = a_{\phi(1)}+...+a_{\phi(n)}$
Seja $n \in \mathbb{N}$, então $t_n \leq a_1+...+a_m$ onde $m= max\{\phi(1),...,\phi(n)\}$ ou seja, $\forall n \in \mathbb{N}$ existe $m \in \mathbb{N}$ tal que $t_n\leq s_m$. Como $s_n$ é monótona e limitada (nesse caso), então $t_n$ também é crescente e limitada e portanto converge. Se $t_n \to t$ e $s_n \to s$, então que $t\leq s$ pois $t_n \leq s_n$. Mas por outro lado, sabemos que para todo $m\in \mathbb{N}$ existe $n \in \mathbb{N}$ tal que $s_m \leq t_n \leq t \Rightarrow lim \ s \leq lim \ t_n \Rightarrow s\leq t \Rightarrow s = t$.
##### Parte 2, $(a_n)$ sinal arbitrário:
Sabemos que como $\sum a_n^+$ e $\sum a_n^-$ são absolutamente convergentes, então em particular elas são convergentes, então pela parte 1, temos que $\sum a_{\phi(n)}^+ < +\infty$ e $\sum a_{\phi(n)}^-<+\infty$ e também que $\sum a_n^+= \sum a_{\phi(n)}^+$ e $\sum a_n^-=\sum a_{\phi(n)}^-$. Logo, $t_n = \sum a_{\phi(k)})^+ - \sum a_{\phi(k)}^-$ então quando $n\to \infty$ $\sum a_n^+ - \sum a_n^-= \sum a_n$ ou seja $t_n, s_n \to s$.

