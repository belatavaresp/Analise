### Definição:
Seja $(x_n)$ uma [[Sequência]], ela é limitada superior ou inferiormente se $X$ for limitado superior ou inferiormente (respectivamente). $(x_n)$ é limitada se $X\subseteq [m,M]$, onde $m,M \in \mathbb{R}$.
### Exemplos:
1. $x_n = c\in \mathbb{R} \iff (x_n) = (c,c,c,c,...)$, $X = \{c\}$ é limitada
2. $x_n=(-1)^n, \ (x_n)=(-1,1,-1,1,-1,1,-1,...), \ X = \{-1,1\}$ é limitada
3. $x_n = n, \ (x_n)=(1,2,3,...), \ X=\mathbb{N}$ é limitada inferiormente
4. $(x_n) =$ alguma enumeração de $\mathbb{Q}$, $X = \mathbb{Q}$ não é limitada.
5.  $a\neq 0, \ x_n=a^n, \ (x_n)=(a, a^2, a^3,...), \ X = \{a,a^2,...\}$, temos que analisar 2 casos:
	1. $a>1$: nesse caso $a^n>a \ \forall a>1$, logo sabemos que a sequência é limitada inferiormente. Para a cota superior, temos pela [[Desigualdade de Bernoulli]] que se $1+x=a \Rightarrow x=a-1 > 0$, então $a^n\geq 1+n(a-1)$. Seja $c>0$ vamos provar que $\exists n\in \mathbb{N}$ tal que $a^n>c$. Sabemos que $1+n(a-1)>c \iff n(a-1)>c-1\iff n>\frac{c-1}{a-1}$ como $\mathbb{N}$ não é limitado superiormente, sempre existe $n\in \mathbb{N}$ que satisfaz. Logo $(x_n)$ não é limitada superiormente
	2. $0<a<1$: aqui sabemos que $max \ X = a = x_1$. $a^n > 0 \Rightarrow X$ é limitado inferiormente. Para a cota superior vamos provar que para qualquer $\epsilon >0 \ \exists n\in\mathbb{N}$ tal que $a^n < \epsilon$. Se $\tilde{a} = \frac{1}{a} > 1$e $c=\frac{1}{\epsilon}>0$ sabemos que existe $n \in \mathbb{N}$ tal que $\tilde{a}^n > c$, então $\frac{1}{a^n}>\frac{1}{\epsilon} \iff a^n < \epsilon$.
