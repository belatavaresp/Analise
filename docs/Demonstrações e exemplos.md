### Exemplo 1:
Prove que $s(n) \neq n \ \ \forall n\in \mathbb{N}$.

**Prova usando [[Indução]]:**
- Caso base:  $s(1) \neq 1$ pelo [[Conjunto dos números naturais#Axioma 2]]
- Passo indutivo: assumimos $s(n) \neq n$, como $s$ é injetiva temos que $s(s(n)) \neq s(n)$. $\Box$ 

### Exemplo 2:
Prove que seja $n \in \mathbb{N}$ então $\nexists p \in \mathbb{N} : n<p<n+1$.

**Prova usando [[Lei do corte]]:**
Suponha que exista $p$. Então sabemos que como $n<p$ então $\exists m \in \mathbb{N}: p = m+n$. Mas pelo mesmo argumento, como $p<n+1$, $\exists q \in \mathbb{N}: n+1 = p+q$. Assim temos então que $n+1 = m+n+q$, mas então pela [[Lei do corte]], $1 = m+q$ o que é absurdo pois 1 não é sucessor de nenhum natural pelo [[Conjunto dos números naturais#Axioma 1]]. $\Box$ 

### Exemplo 3:
Prove que, sendo $X$ um conjunto, se existe $\phi_1: I_n \rightarrow X$ e $\phi_2: I_m \rightarrow X$ bijeções, então $n=m$.

**Prova:**
Suponha $m<n$. $I_m \rightarrow X \rightarrow I_n \Rightarrow \phi_2 \circ \phi_1^{-1}$ é uma bijeção, que é uma contradição com o [[Conjunto finito#Teorema 1]]. $\Box$ 

### Exemplo 4:
Prove que $\mathbb{Q}$ é enumerável.

**Prova:**
Defina $\phi: \mathbb{Z} \times \mathbb{Z}^* \rightarrow \mathbb{Q}$ tal que $\phi(p,q) = \frac{p}{q}$ então, pelo [[Enumerável#Corolário 4]], temos uma função sobrejetiva entre um conjunto enumerável e $\mathbb{Q}$, logo, pelo [[Enumerável#Corolário 3]] ele também é um conjunto enumerável. $\Box$ 

### Exemplo 5:
O conjunto $X = \{ \text{ sequências com entradas 0 ou 1}\} = \{1,0\}^{\mathbb{N}}$ não é enumerável.

**Prova:**
Diagonalização de Cantor.
Supomos pelo absurdo que $X$ é enumerável. Seja $f: \mathbb{N} \rightarrow X$ bijeção, denotamos $s_n = f(n)$.
Seja $s_n = (s_{n1}, s_{n2}, ..., s_{nj}, ...)$ e assim em diante, é sempre possível criar um elemento $s* = (1- s_{11}, ..., 1-s_{nn}, ...)$ tal que $s* \in X: s* \neq s_i \ \forall i$ e portanto não está contemplado pela enumeração $f$, absurdo. $\Box$ 

### Exemplo 6:
$card(\mathbb{N}) < card(P(\mathbb{N}))$ 

**Prova:**
Vamos criar uma bijeção entre $P(\mathbb{N})$ e $X = \{0,1\}^{\mathbb{N}}$. Para cada elemento de $\mathbb{N}$ vamos associar $1$ caso ele pertença à um subconjunto de $P(\mathbb{N})$ ou $0$ caso contrário. Note que isso evidencia que $P(\mathbb{N}) = X$ e pelo [[Demonstrações e exemplos#Exemplo 5]] ele é não enumerável, portanto pelo  [[Enumerável#Teorema 1]] $card(\mathbb{N}) < card(P(\mathbb{N}))$. $\Box$    

### Exemplo 7:
$\mathbb{R}$ é não enumerável.

**Prova:**
Basta escrever os reais em $[0,1]$ como $z \in [0,1]: z = 0, d_1 d_2...d_j... \ e \ d_j \in\{0,1\}$, ou seja, em base $2$, e assim ele é análogo ao conjunto $X = \{0,1\}^{\mathbb{N}}$ que pelo [[Demonstrações e exemplos#Exemplo 5]] é não enumerável. 

### Exemplo 8:
Demonstração de [[Corpo ordenado#Propriedades]] **O2**.

**Prova:**
Sejam $x,y \in \mathbb{K}$, consideramos $z = y-x$.
1. $z \in \mathbb{K}^+\iff x<y$
2. $z = 0 \Rightarrow x = y$
3. $-z \in \mathbb{K}^+ \Rightarrow x-y \in \mathbb{K}^+ \iff x>y$ 

### Exemplo 9:
Seja $X \subseteq \mathbb{K}$ onde $\mathbb{K}$ é um [[Corpo ordenado]] definido como $X = \{r \in \mathbb{Q}, r>0 \ | \ r^2 <2\}$.
1. 0 é [[Cota inferior]]
2. 1000 é [[Cota superior]]
3. $X$ é limitado.

