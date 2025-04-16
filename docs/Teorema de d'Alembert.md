Seja $a_n \neq 0, \frac{|a_{n+1}|}{|a_n|}\leq c<1 \Rightarrow$ $a_n$ é uma [[Série absolutamente convergente]].

### Demonstração:
$\frac{|a_{n+1}|}{|a_n|}\leq \frac{c^{n+1}}{c^n} \iff \frac{|a_{n+1}|}{c^{n+1}}\leq \frac{|a_n|}{c^n}$ e portanto $(\frac{|a_n|}{c_n})$ é limitada e $\sum c^n <+\infty$ e portanto pelo [[Série numérica#Teorema 3]] que $a_n$ é absolutamente convergente.

###### OBS (Teste da razão):
$\frac{|a_{n+1}|}{|a_n|} \to l$ temos os casos:

1. $l<1 \Rightarrow \sum |a_n| <+\infty$ e portanto existe $c>0$ tal que $\frac{|a_{n+1}|}{|a_n|}\leq c<1, n\in\mathbb{N}$
2. $l>1$ então existe $N\in\mathbb{N}$ tal que se $n\geq N \Rightarrow \frac{|a_{n+1}|}{|a_n|}\geq c>1$ mas isso implica que $|a_{n+1}|\geq c \cdot |a_n| \geq |a_n| \neq 0 \Rightarrow a_n \not \to 0 \Rightarrow \sum a_n$ diverge.
3. $l=1$, nesse caso não podemos concluir muitas coisas, pois temos séries que funcionam e séries que não funcionam. Por exemplo $\sum \frac{1}{n} \Rightarrow \frac{|a_{n+1}|}{|a_n|} \to 1$ mas $\sum \frac{1}{n}$ diverge.