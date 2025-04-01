### Definição
Seja $\mathbb{K}$ um [[Corpo]] com um subconjunto $\mathbb{K}^+ \subseteq \mathbb{K}$ tal que:

1. $x,y\in \mathbb{K}^+ \Rightarrow xy, x+y \in \mathbb{K}^+$
2. $x \in \mathbb{K} \Rightarrow$ Ocorre **exatamente** uma das três alternativas a seguir:
	1. $x \in \mathbb{K}^+$
	2. $x = 0$
	3. $-x \in \mathbb{K}^+$ 
Então $\mathbb{K}$ é um corpo ordenado e $\mathbb{K}^+$ é chamado de cone positivo.
##### OBS:
Se $\mathbb{K}$ é um corpo ordenado e $x \neq 0: \ x^2 = x \cdot x = (-x)(-x) \Rightarrow x^2\in \mathbb{K}^+$. Em particular, $1 = 1\cdot1 \in \mathbb{K}^+$ 
#### Exemplos:
1. $\mathbb{K} = \mathbb{Q}:  \mathbb{K}^+ = \mathbb{Q}^+$
2. $\mathbb{K} = \mathbb{R}:  \mathbb{K}^+ = \mathbb{R}^+$
3. Não ordenado $\rightarrow \mathbb{C}$ pois não existe $\mathbb{K}^+$ já que $-1$ e $1$ teriam que pertencer a $\mathbb{K}^+$.

### Relação de ordem
Seja $\mathbb{K}$ um corpo ordenado, definimos a relação $<$ como segue:
$$
x<y \iff y-x \in \mathbb{K}^+
$$
##### Notação:
1. $y>x \iff x<y$
2. $x\leq y \iff$ ou $x<y$ ou $x=y$
3. $x\leq y \iff y\geq x$
#### Propriedades:
- **O1:** (Transitiva) $x < y$ e $y<z \Rightarrow x<z$
- **O2:** (Tricotomia) Dados $x,y,z \in \mathbb{K}$, temos **exatamente** uma das alternativas abaixo:
	1. ou $x<y$
	2. ou $x=y$
	3. ou $x > y$
- **C1:** $x<y \Rightarrow x+z < y+z$
- **C2:** $x<y, z>0 \Rightarrow xz<yz$
###### OBS:
- **O1** e **O2**: $<$ é uma relação de ordem total
- **C1** + **C2**: compatibilidade de $<$ com $+$ e $\cdot$
- Dentro de um corpo ordenado $\mathbb{K}$ sempre conseguimos encontrar subconjuntos análogos aos conjuntos $\mathbb{N}\subset \mathbb{Z} \subset \mathbb{Q}$ .

### Valor absoluto
Seja $x \in \mathbb{K}$
$$
|x| = \begin{cases}x & x\geq0 \\ -x & x<0 \end{cases} = max(x,-x)
$$
#### Desigualdade Triangular
Sejam $x,y \in \mathbb{K}$, $|x+y| \leq |x|+|y|$.
##### Demonstração:
$|x| \geq x$ e $|y| \geq y$, logo $x+y \leq |x+y|$. Analogamente $-x \leq |x|$ e $-y \leq |y|$ então $-(x+y) \leq |x| - |y|$Então $|x-y| = max\{x+y, -(x+y)\} \leq |x|+|y|$ $\Box$.

### Limites
Seja $\mathbb{K}$ um corpo ordenado e $X \subseteq \mathbb{K}$ se $X$ possui [[Cota superior]] $M$ dizemos que ele é **limitado superiormente**. Analogamente, se $X$ possui [[Cota inferior]] $m$ dizemos que ele é **limitado inferiormente**. Se existem ambos $M$ e $m$ então dizemos que $X$ é **limitado**.