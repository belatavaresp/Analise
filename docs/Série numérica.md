### Definição:
Dado um **termo geral** definido por uma [[Sequência]] $a_n$, definimos uma série como: $s_1=a_1, s_2 = a_1+a_2, ..., s_n = a_1+...+a_n$ onde a [[Sequência]] $(s_n)$ é chamada **somas parciais** da série.

### Convergência:
$(s_n) \to s$ se a série $\sum{a_n}$ converge e sua soma é $s$, e diverge quando $\sum{a_n}$ é divergente.
#### Exemplos:
1. Série geométrica: $0<|a|<1$, onde $\sum a^n$ converge e $s_n = 1+a+...+a^n = \frac{1-a^{n+1}}{1-a} \to \frac{1}{1-a} = s$
2. $\sum{\frac{1}{n!}} = 1+1+\frac{1}{2!}+...=e$
3. $\sum{1}, s_n = n$ é divergente
4. $\sum(-1)^{n+1} = 1-1+1-1..., s_1 = 1, s_2 = 0, s_3 = 1, ...$ é divergente
5. Série telescópica: $\sum{\frac{1}{n(n+1)} = \frac{1}{n}-\frac{1}{n+1}}, s_n = 1-\frac{1}{n+1}, s_n \to 1$ 
6. Série harmônica: $\sum{\frac{1}{n}}$ é divergente

**OBS:**
$a_n\geq 0, \ \forall n \in \mathbb{N} \Rightarrow (s_n)$ é crescente, então $(s_n)$ converge $\iff \ \exists M>0: s_n\leq M$
##### Notação:
1. $\sum a_n$ converge $\iff \sum a_n < +\infty$
2. $\sum a_n$ diverge $\iff \sum a_n = +\infty$

### Teorema 1:
Se $\sum a_n$ converge $\Rightarrow a_n \to 0$
#### Demonstração:
$s_{n+1} = s_n + a_n$ mas $lim \ s_{n+1} = lim \ s_n = s$ e portanto $lim \ a_n = 0$.

### Teorema 2:
Se $\sum a_n$ é uma [[Série absolutamente convergente]] $\Rightarrow \sum a_n$ converge.
#### Demonstração:
Sejam $x^+$ e $x^-$ definidos como:
$$
x^+ = \begin{cases}
x, & \text{if } x \geq 0 \\
0, & \text{if } x < 0
\end{cases}
$$
$$
x^- = \begin{cases}
-x, & \text{if } x \leq 0 \\
0, & \text{if } x > 0
\end{cases}
$$
Temos que $|x| = x^+ + x^-$ onde $x^+, x^- \leq |x|$ e $x = x^+-x^-$. Então obtemos:

1. Como $a_n^+\leq|a_n|$, pelo [[Teorema do critério da comparação]] $\Rightarrow \sum a_n^+<+\infty$
2. Como $a_n = a_n^+ - a_n^-$ e por 1. sabemos que $a_n^+$ e $a_n^-$ convergem, então como a diferença de séries convergentes também é convergente $\Rightarrow \sum a_n$ converge.

### Teorema 3:
Seja $b_n \neq 0$, $(\frac{a_n}{b_n})$ limitada e $\sum |b_n| <+\infty \Rightarrow \sum a_n$ é uma [[Série absolutamente convergente]]
#### Demonstração:
$|a_n| = \frac{|a_n|}{|b_n|}\cdot |b_n|\leq M \cdot |b_n|$ onde sabemos que $M$ existe pois $\frac{a_n}{b_n}$ é limitada, logo pelo [[Teorema do critério da comparação]] $\Rightarrow \sum|a_n|<+\infty$.

#### Exemplo:
$a_n=\sum \frac{1}{n^2-3n+1}$ como para algum $n$ sabemos que a série fica com termos apenas positivos. Seja $b_n = \sum \frac{1}{n^2}$, vamos mostrar que $\frac{a_n}{b_n}$ é limitada.
Para $n\geq 2$ temos que $\frac{|a_n|}{|b_n|} = \frac{\frac{1}{n^2-3n+1}}{\frac{1}{n^2}} = \frac{n^2}{n^2-3n+1}$ dividindo por $n^2$ temos $\frac{1}{1-\frac{3}{n}+\frac{1}{n^2}}\to 1$.

### Teorema 4:
Seja $a_n \neq 0$ tal que vale o [[Teorema de d'Alembert]] ou seja $\frac{|a_{n+1}|}{|a_n|}\to l \Rightarrow$ vale o [[Teorema de Cauchy]] ou seja $\sqrt[n]{|a_n|}\to l$. Em termos teóricos, isso quer dizer que o teste da raiz é mais forte que o teste da razão (a recíproca do teorema não vale).

#### Exemplo:
$a_n = \frac{n^n}{n!}$ então $\frac{a_{n+1}}{a_n} = (1+\frac{1}{n})^n\to e \Rightarrow \sqrt[n]{a_n}\to e \Rightarrow \frac{n}{\sqrt[n]{n!}} \to e$ ou seja para $n$ "grande" temos que $n \approx e \cdot \sqrt[n]{n!}$. 
