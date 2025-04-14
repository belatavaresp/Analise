### Exemplo 1:
Prove que $s(n) \neq n \ \ \forall n\in \mathbb{N}$.

**Prova usando [[Indução]]:**
- Caso base:  $s(1) \neq 1$ pelo [[Conjunto dos números naturais#Axioma 2]]
- Passo indutivo: assumimos $s(n) \neq n$, como $s$ é injetiva temos que $s(s(n)) \neq s(n)$. $\Box$ 

---
### Exemplo 2:
Prove que seja $n \in \mathbb{N}$ então $\nexists p \in \mathbb{N} : n<p<n+1$.

**Prova usando [[Lei do corte]]:**
Suponha que exista $p$. Então sabemos que como $n<p$ então $\exists m \in \mathbb{N}: p = m+n$. Mas pelo mesmo argumento, como $p<n+1$, $\exists q \in \mathbb{N}: n+1 = p+q$. Assim temos então que $n+1 = m+n+q$, mas então pela [[Lei do corte]], $1 = m+q$ o que é absurdo pois 1 não é sucessor de nenhum natural pelo [[Conjunto dos números naturais#Axioma 1]]. $\Box$ 

---
### Exemplo 3:
Prove que, sendo $X$ um conjunto, se existe $\phi_1: I_n \rightarrow X$ e $\phi_2: I_m \rightarrow X$ bijeções, então $n=m$.

**Prova:**
Suponha $m<n$. $I_m \rightarrow X \rightarrow I_n \Rightarrow \phi_2 \circ \phi_1^{-1}$ é uma bijeção, que é uma contradição com o [[Conjunto finito#Teorema 1]]. $\Box$ 

---
### Exemplo 4:
Prove que $\mathbb{Q}$ é enumerável.

**Prova:**
Defina $\phi: \mathbb{Z} \times \mathbb{Z}^* \rightarrow \mathbb{Q}$ tal que $\phi(p,q) = \frac{p}{q}$ então, pelo [[Enumerável#Corolário 4]], temos uma função sobrejetiva entre um conjunto enumerável e $\mathbb{Q}$, logo, pelo [[Enumerável#Corolário 3]] ele também é um conjunto enumerável. $\Box$ 

---
### Exemplo 5:
O conjunto $X = \{ \text{ sequências com entradas 0 ou 1}\} = \{1,0\}^{\mathbb{N}}$ não é enumerável.

**Prova:**
Diagonalização de Cantor.
Supomos pelo absurdo que $X$ é enumerável. Seja $f: \mathbb{N} \rightarrow X$ bijeção, denotamos $s_n = f(n)$.
Seja $s_n = (s_{n1}, s_{n2}, ..., s_{nj}, ...)$ e assim em diante, é sempre possível criar um elemento $s* = (1- s_{11}, ..., 1-s_{nn}, ...)$ tal que $s* \in X: s* \neq s_i \ \forall i$ e portanto não está contemplado pela enumeração $f$, absurdo. $\Box$ 

---
### Exemplo 6:
$card(\mathbb{N}) < card(P(\mathbb{N}))$ 

**Prova:**
Vamos criar uma bijeção entre $P(\mathbb{N})$ e $X = \{0,1\}^{\mathbb{N}}$. Para cada elemento de $\mathbb{N}$ vamos associar $1$ caso ele pertença à um subconjunto de $P(\mathbb{N})$ ou $0$ caso contrário. Note que isso evidencia que $P(\mathbb{N}) = X$ e pelo [[Demonstrações e exemplos#Exemplo 5]] ele é não enumerável, portanto pelo  [[Enumerável#Teorema 1]] $card(\mathbb{N}) < card(P(\mathbb{N}))$. $\Box$    

---
### Exemplo 7:
$\mathbb{R}$ é não enumerável.

**Prova:**
Basta escrever os reais em $[0,1]$ como $z \in [0,1]: z = 0, d_1 d_2...d_j... \ e \ d_j \in\{0,1\}$, ou seja, em base $2$, e assim ele é análogo ao conjunto $X = \{0,1\}^{\mathbb{N}}$ que pelo [[Demonstrações e exemplos#Exemplo 5]] é não enumerável. 

---
### Exemplo 8:
Demonstração de [[Corpo ordenado#Propriedades]] **O2**.

**Prova:**
Sejam $x,y \in \mathbb{K}$, consideramos $z = y-x$.
1. $z \in \mathbb{K}^+\iff x<y$
2. $z = 0 \Rightarrow x = y$
3. $-z \in \mathbb{K}^+ \Rightarrow x-y \in \mathbb{K}^+ \iff x>y$ 

---
### Exemplo 9:
Seja $X \subseteq \mathbb{K}$ onde $\mathbb{K}$ é um [[Corpo ordenado]] definido como $X = \{r \in \mathbb{Q}, r>0 \ | \ r^2 <2\}$.
1. 0 é [[Cota inferior]]
2. 1000 é [[Cota superior]]
3. $X$ é limitado.

---
### Exemplo 10:
Seja $x_n>0$ uma [[Sequência]] onde $\frac{x_{n+1}}{x_n}\to a<1$. Mostre que $x_n \to 0$.

**Prova:**
$x_n$ decresce "a partir de algum $N$". Seja $b\in(a,1) \Rightarrow lim\frac{x_{n+1}}{x_n} = a < b< 1$.
Existe $N \in \mathbb{N}$ tal que $n \geq N \Rightarrow \frac{x_{n+1}}{x_n} < b < 1 \Rightarrow x_{n+1} < x_n$. Vamos mostrar que se $x_n$ converge para o [[Limite]] $l$, temos que $l=0$ pois como $x_{n+1} < b\cdot x_n$ então $lim \ x_{n+1} \leq lim \ b \cdot x_n$  ou seja, $l \leq bl \Rightarrow (b-1)l \geq 0$ mas $b-1 < 0$ então como $x_n>0 \Rightarrow l\geq 0$ mas como $(b-1)l\geq 0 \Rightarrow l=0$.

---
### Exemplo 11:
Sabendo que $n^k << a^n << n! << n^n$ onde $a>1, k\in \mathbb{N}$. Vamos mostrar que $lim \frac{n^k}{a^n}=0$.

**Prova:**
Defina $x_n = \frac{n^k}{a^n} >0$. Então $\frac{x_{n+1}}{x_n} = \frac{\frac{(n+1)^k}{a^{n+1}}}{\frac{n^k}{a^n}} = \frac{1}{a}(\frac{n+1}{n})^k = \frac{1}{a}(1+\frac{1}{n})^k$. Como $1+\frac{1}{n} \to 1$ então $(1+\frac{1}{n})^k \to 1^k = 1$ e portanto $\frac{x_{n+1}}{x_n} \to \frac{1}{a} < 1$. Então pelo [[Demonstrações e exemplos#Exemplo 10]] sabemos que $x_n \to 0$. 

**OBS:** Isso pode ser provado analogamente para $lim \frac{a^n}{n!}=lim\frac{n!}{n^n}=0$.

---
### Exemplo 12:
Seja $x_n = a^{\frac{1}{n}}$ onde $a>0$. Mostre que $(x_n)$ converge para 1.

**Prova:**
Sabemos que $x_n$ é monótona pois se $a>1 \Rightarrow a^{\frac{1}{n}}$ decresce e se $a>1$ cresce. Além disso sabemos que ela é limitada pois se $a>1, a^{\frac{1}{n}} > 1 \Rightarrow x_n$ converge e se $a<1 \Rightarrow a^{\frac{1}{n}} < 1$ e nesse caso $x_n$ também converge.
Seja $l$ o [[Limite]] de $x_n$, então a subsequência $x_{n(n+1)}\to l$. Mas como $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$ (truque!), então $x_{n(n+1)} = a^{\frac{1}{n} - \frac{1}{n(n+1)}} = \frac{a^{\frac{1}{n}}}{a^{\frac{1}{n+1}}} \to \frac{l}{l} = 1$ e portanto o limite deve ser 1.

---
### Exemplo 13:
Seja $a\in(0,1)$ e $x_n = 1+a+a^2+...+a^n$, mostre que $x_n \to \frac{1}{1-a}$.

**Prova:**
$x_n = (1+a+...+a^n)\frac{(1-a)}{1-a} = \frac{1-a^{n+1}}{1-a} \to \frac{1}{1-a}$ pois $a\in(0,1)$.

---
### Exemplo 14:
Seja $x_n = \frac{1}{0!} + ... + \frac{1}{n!}$, mostre que $x_n$ converge.

**Prova:**
Sabemos que $x_n$ é estritamente crescente.
%% Exercício + provar que $n!\geq 2^{n-1}$ (fazer indução) %% .
Vamos mostrar que ela é limitada. Sabemos que $x_n \leq 1+1+\frac{1}{2}+...+\frac{1}{2^{n-1}}$ e sabemos pelo [[Demonstrações e exemplos#Exemplo 13]] que o lado direito converge para $1+\frac{1}{1-\frac{1}{2}} = 3$ então $x_n,<3$. Como ela é uma [[Sequência monótona]] e uma [[Sequência limitada]] então ela converge para algum limite (nesse caso $e$, mas não precisamos encontrar o limite).

---
### Exemplo 15:
Mostre que $a_n = (1+\frac{1}{n})^n \to e$.

**Prova:**
Vamos mostrar que $a_n$ é crescente. Pela expansão do binômio de $a_n$ temos que $a_n = 1+1+\frac{n(n+1)}{2!}\frac{1}{n^2} + ... + \frac{n!}{n!}\frac{1}{n^2} = 1+1+...+\frac{1}{n!}(1-\frac{1}{n})(1-\frac{2}{n})...\frac{2}{n}\frac{1}{n}$ e analisando essa estrutura percebemos que $a_n < a_{n+1}$
Seja $x_n$ a sequência do [[Demonstrações e exemplos#Exemplo 14]], sabemos que $a_n \leq x_n \ \forall n \in\mathbb{N}$ e portanto sabemos que $a_n \to l$ para algum valor de $l$.
Por fim temos que se $k$ é fixo e $n\geq k \Rightarrow a_n \geq 1+1+...+\frac{1}{k!}(1-\frac{1}{k})(1-\frac{2}{k})...(1-\frac{k-1}{n})$ então $lim \ a_n = l\geq 1+1+\frac{1}{2!}+...+\frac{1}{k!} = x_k$ (limite do lado direito da desigualdade) mas então como $a_n\leq x_n < e$ temos que $l\leq e$ e $e\leq l \Rightarrow l=e$.
**OBS:**
Note que não podemos usar o fato de que o limite interno é 1 pois isso implicaria que $x_n \to 1 \neq e$.

---
### Exemplo 16:
Mostre a convergência de $\sum \frac{1}{n^r}, r\in\mathbb{R}$ para os valores possíveis de $r$.

**Prova:**
1. $r<1$, nesse caso $n^r<n \Rightarrow \frac{1}{n^r}>\frac{1}{n}$, mas $\sum \frac{1}{n} = +\infty$ então pelo [[Teorema do critério da comparação]] a série diverge.
2. $r>1$, nesse caso, $(s_n)$ é crescente, logo $s_n$ converge $\iff \ \exists (s_{n_k})_k$ convergente. Vamos escolher $n_k = 2^k-1$, ou seja $s_{2^k-1} = 1+ \left(\frac{1}{2^r} + \frac{1}{3^r}\right) + \left(\frac{1}{4^r} + \frac{1}{5^r} + \frac{1}{6^r} + \frac{1}{7^r}\right) + \dots + \left(\frac{1}{(2^{k-1})^r} + \dots + \frac{1}{(2^k - 1)^r} \right) \leq 1+\frac{1}{2^{r-1}} + ... + \frac{1}{(2^{r-1})^{k-1}}$ como $0 < a = \frac{1}{2^{r-1}} < 1$ pois $r>1$ então existe $M>0$ tal que $s_{{2^k} - 1} \leq M$ pois ela é uma versão da série geométrica. Logo $(s_n)$ converge quando $r>1$. 
3. $r=0$, então $\sum \frac{1}{n^r} = \sum 1$ que sabemos que diverge.

**OBS:**
Essa série é conhecida como *Zeta de Riemann* e é muito estudada atualmente, e pode ser utilizada para encontrar a convergência de outras séries a partir do [[Teorema do critério da comparação]].

---
