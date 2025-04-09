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

### Teorema 5:
Seja $x_n$ uma [[Sequência]] que converge para um limite $l$.

1. $l > a \Rightarrow \exists n_1 \in \mathbb{N}: n\geq n_1 \Rightarrow x_n > a$ 
2. $l< a \Rightarrow \exists n_2 \in \mathbb{N}: n\geq n_2 \Rightarrow x_n < a$ 
#### Demonstração:
1. Como $x_n \to l$ seja $\epsilon = l-a$, sabemos que $\forall \epsilon>0, \exists n_1 \in \mathbb{N}: n\geq n_1 \Rightarrow l-\epsilon < x_n < l+\epsilon$ logo para a nossa escolha de $\epsilon$ obtemos que $x_n > a$.
2. Análogo ao caso anterior.
#### Corolário 1:
$x_n \to l \Rightarrow$ Existe $N \in \mathbb{N}$ tal que $n\geq N \Rightarrow x_n > 0$ e em especial $x_n > \frac{l}{2}$.
##### Demonstração:
A mesma do Teorema 5. Sai diretamente de que $x_n \to l > \frac{l}{2}$ pois $l>0$.
#### Corolário 2:
$x_n \to l_1$ e $y_n \to l_2$ tais que $x_n\leq y_n$ para todo $n\geq N$ onde $N \in \mathbb{N} \Rightarrow l_1\leq l_2$.
##### Demonstração:
Suponha que $l_1 > l_2$. Seja $c \in (l_2,l_1)$ pelo item 2 do Teorema 5 temos que $y_n < c, n \geq N_1$ e que $x_n > c, n\geq N_2$. Logo $\exists N_3 = max\{N_1, N_2\}$ tal que se $n\geq N_3 \Rightarrow x_n > c > y_n$ que é contradição. 

**OBS:**
Se temos $x_n = 0$ e $y_n = \frac{1}{n}$ então $x_n < y_n$ mas ambas as sequências convergem para 0. Em geral, quando temos desigualdades estritas, elas não permanecem estritas após tirar o limite.

### Teorema 6:
Seja $x_n \to 0$ e $y_n$ uma [[Sequência limitada]]. Então $z_n = x_ny_n \to 0$.
#### Demonstração:
Como $y_n$ é limitada $\iff \exists M>0: |y_n|\leq M \ \forall n\geq N \in \mathbb{N}$. Seja $\epsilon > 0$ e seja $N = N_{\frac{\epsilon}{M}}$ (valor de $N$ da convergência para $\epsilon = \frac{\epsilon}{M}$) tal que $n\geq N \Rightarrow |x_n| < \frac{\epsilon}{M}$. Então $n\geq N$ vale que $|x_ny_n| = |x_n||y_n| \leq M|x_n| < M\cdot \frac{\epsilon}{M} = \epsilon$. 
##### Exemplo:
$x_n = \frac{1}{n}, y_n = sen(2^nn!)$ então $\frac{sen(2^nn!)}{n} \to 0$.

### Teorema 7:
Seja $x_n \to l_1$ e $y_n \to l_2$ sequências.

1. $x_n \pm y_n \rightarrow l_1 \pm l_2$
2. $x_ny_n \rightarrow l_1l_2$
3. $\frac{x_n}{y_n} \to \frac{l_1}{l_2}$ se $l_2 \neq 0$
#### Demonstração:
1. $|(x_n+y_n) - (l_1+l_2)| = |(x_n - l_1)+(y_n - l_2)| \leq |x_n-l_1| + |y_n - l_2|$. Como $x_n\to l_1 \Rightarrow \exists N_1 : n\geq N_1 \Rightarrow |x_n-l_1|<\frac{\epsilon}{2}$ e analogamente $\exists N_2$ para $y_n$ então $|x_n -l_1|+|y_n -l_2| < \frac{\epsilon}{2}+\frac{\epsilon}{2} = \epsilon$.
2. Queremos mostrar que $|x_ny_n -l_1l_2|< \epsilon$ se $n\geq N$. Simplificando $x_ny_n-l_1l_2 = x_n(y_n-l_2)+l_2(x_n-l_1)$ mas sabemos que $y_n \to l_2$ portanto $(y_n -l_2) \to 0$ e $(x_1-l_1)\to 0$ analogamente. Como sabemos que $x_n\to l_1$ então ela é limitada, portanto pelo [[Limite#Teorema 6]] $x_n(y_n-l_2)+l_2(x_n-l_1) \to 0+0 = 0$ e assim mostramos que $(x_ny_n-l_1l_2) \to 0$ e portanto $x_ny_n \to 0$.
3. Vamos mostrar que $\frac{1}{y_n}\to \frac{1}{l_2}$ para utilizar 2. com $x_n$ e $\frac{1}{y_n}$ e mostrar o enunciado. Sabemos que $\frac{1}{y_n}-\frac{1}{l_2} = \frac{l_2-y_n}{y_nl_2} = (l_2-y_n)\frac{1}{y_nl_2}$. Então vamos provar que $(\frac{1}{y_n})_n$ é limitada. Sabemos que $y_n \to l_2 \neq 0$, suponha $l_2>0$, então pelo [[Limite#Corolário 1]] existe um $N\in \mathbb{N}: n\geq N \Rightarrow y_n>\frac{l_2}{2}$ e assim $|\frac{1}{y_n}| = \frac{1}{|y_n|} < \frac{2}{|l_2|}$ para $n\geq N$. Por fim $(l_2-y_n)\frac{1}{y_nl_2} \to 0$ pois $(l_2-y_n)\to 0$ e $\frac{1}{y_nl_2}$ é limitada como mostramos.