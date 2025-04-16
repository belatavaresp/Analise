Seja $\sqrt[n]{|a_n|} \leq c<1$ e $n\geq 1 (n\geq N) \Rightarrow$ $a_n$ é uma [[Série absolutamente convergente]].

### Demonstração:
$|a_n|\leq c^n$ então pelo [[Série numérica#Teorema 3]] $a_n$ é absolutamente convergente.

###### OBS (Teste da raiz):
$\sqrt[n]{|a_n|}\to l$ temos os casos:

1. $l<1$: então $\sum |a_n| \leq \infty$ e portanto $\sqrt[n]{|a_n|}\leq c <1, n\geq N$
2. $l>1$: então $\sqrt[n]{|a_n|} > 1, n\leq N \Rightarrow a_n \not \to 0 \Rightarrow \sum a_n$ diverge (concluímos isso sobre a série toda!)
3. $l=1$: então não podemos concluir muita coisa, pois existem séries que funcionam e séries que não funcionam, por exemplo: $\sum \frac{1}{n} = \infty, \sqrt[n]{\frac{1}{n}}\to 1$

### Exemplos:
1. $\sum (\frac{\log{n}}{n})^n < +\infty$ para $n\leq 3$, pois $\frac{\log(n)}{n} = \sqrt[n]{(\frac{\log{n}}{n})^n} \to 0$. Note que também podemos concluir que $\sum \frac{\log{n}}{n}, n\geq 3 > \sum \frac{1}{n}$ que diverge, e portanto essa série também diverge.