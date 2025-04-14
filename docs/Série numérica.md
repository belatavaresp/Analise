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
$a_n\geq 0, \ \forall n \in \mathbb{N} \Rightarrow (s_n)$ é crescente, portanto $(s_n)$ converge $\iff \ \exists M>0: s_n\leq M$
##### Notação:
1. $\sum a_n$ converge $\iff \sum a_n < +\infty$
2. $\sum a_n$ diverge $\iff \sum a_n = +\infty$

### Teorema:
Se $\sum a_n$ converge $\Rightarrow a_n \to 0$
#### Demonstração:
$s_{n+1} = s_n + a_n$ mas $lim \ s_{n+1} = lim \ s_n = s$ e portanto $lim \ a_n = 0$.