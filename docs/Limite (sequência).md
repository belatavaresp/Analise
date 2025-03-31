### Definição:
A [[Sequência]] $(x_n)$ tem limite $l\in \mathbb{R}$ se para todo $\epsilon >0$, existe $N \in \mathbb{N}$ tal que $n\geq N \Rightarrow |x_n-l|<\epsilon$ ou seja, $x_n \in V_{\epsilon}(l)$, que é a [[Vizinhança]] de raio $\epsilon$ ao redor do limite.

#### Notação:
$x_n \rightarrow l \iff x_n\rightarrow l, n\rightarrow \infty \iff \lim_{n \to \infty} x_n = l$. 
Uma sequência $(x_n)$ pode ser convergente, se possui limite, e divergente se não o possui.

### Teorema 1 (Unicidade):
Uma sequência não pode convergir para dois limites distintos.
#### Demonstração:
Suponha $x_n \to l$ e seja $b\neq l$. Seja $\epsilon > 0$ tal que $(l-\epsilon, l+\epsilon) \cap (b-\epsilon, b+\epsilon) = \emptyset$. Pela definição, existe $N_{\epsilon} \in \mathbb{N}$ tal que $x_n \in (l-\epsilon, l+\epsilon)$ para todo $n\geq N_{\epsilon}$. Portanto a vizinhança $V_{\epsilon}(b) = (b-\epsilon, b+\epsilon)$ pode conter uma quantidade finita de termos de $(X_n)$ concluímos então que $X_n \not \to b$. $\Box$.

### Teorema 2:
Se $x_n \to l$ então qualquer [[Subsequência]] converge para o mesmo limite.
#### Exemplos:
1. $x_n = c, \ x_n \to c$
2. $x_n = (-1)^n, \ x_n$ diverge pois $x_{2n} \to 1$ e $x_{2n-1} \to -1$ 
#### Demonstração:
Seja $(x_{n_k}) = (x_{n_1}, x_{n_2}, ...)$ uma subsequência de $x_n$. Como $x_n \to l \iff \forall \epsilon>0, \ \exists N\in \mathbb{N}: |x_n-l|<\epsilon \ \forall n\geq N$. Seja $x_k$ o elemento de $x_{n_k}$ tal que $x_k\geq N$ e portanto para todo $x_{n_k} \geq n_k$ temos que $|x_{n_k}| < \epsilon$ e portanto $x_{n_k}\to l$. $\Box$.

### Teorema 3:
Toda sequência convergente é uma [[Sequência limitada]].
#### Demonstração:
Como $x_n \to n$ então existe $N\in\mathbb{N}: \ \forall n\geq N$ vale que $l-1<x_n<l+1$ (escolhemos $\epsilon = 1$).
Seja $B = max\{x_1,x_2,...,x_{N-1}, l+1\}$. Então $x_n \leq B \ \forall n\in\mathbb{N}$.
Seja $A = min\{x_1,x_2,...,x_{N-1}, l-1\}$. Então $x_n\geq A \ \forall n \in \mathbb{N}$.
Logo $x_n \in [A,B] \ \forall n \in \mathbb{N}$. $\Box$.

### Teorema 4:
Toda [[Sequência monótona]] e que é também [[Sequência limitada]] converge.
#### Demonstração:
Seja $x_n$ crescente. Vamos provar que $x_n \to l = sup\{x_n \ | \ n\in \mathbb{N}\}$. Seja $\epsilon >0$, como $l-\epsilon$ não é [[Cota superior]] de $X = \{x_n \ |\ n\in\mathbb{N}\}$ então $\exists N \in \mathbb{N}$ tal que $l-\epsilon<x_N\leq l$. Como $x_n$ é crescente $\Rightarrow x_n\geq x_N$ se $n\geq N$. Portanto, $n\geq N \Rightarrow l-\epsilon<x_N\leq x_n\leq l<l+\epsilon$, logo $x_n \in (l-\epsilon,l+\epsilon)$.
O resultado é análogo quando $x_n$ é decrescente.
#### Exemplos:
1. $x_n = \frac{1}{n}$, $inf\{\frac{1}{n} \ | \ n \in \mathbb{N}\} = 0$ logo $x_n \to 0$.
2. Seja $0<a<1$ e $x_n = a^n$ a sequência decrescente, como $inf\{a^n \ | \ n\in \mathbb{N}\} = 0$ então $x_n \to 0$.

