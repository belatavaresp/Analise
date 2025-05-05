Toda [[Sequência]] que limitada tem alguma [[Subsequência]] convergente.
### Demonstração:
Note que $a_n-b_n \to 0$ então existe $c\in \mathbb{R}$ tal que $\bigcup_{n=1}^{\infty} I_n = \{c\}$ pelo [[Teorema dos intervalos encaixados]].

Sejam $a_1$ e $b_1$ tais que $a_1 \leq x_n \leq b_1 \ \forall n\in \mathbb{N}$. Seja $I_1 = [a_1,b_1]$ e $n_1\in \mathbb{N}$. Se dividimos o intervalo de $a_1$ até $\frac{a_1+b_1}{2}$ e de $\frac{a_1+b_1}{2}$ até $b_1$ temos os casos:
1. Há uma quantidade infinita de termos de $(x_n)$ no intervalo $[a_1,\frac{a_1+b_1}{2}]$. Então fazemos $a_2=a_1$ e $b_2 = \frac{a_1+b_1}{2}$ e $x_{n_2}$ tal que:
	1. $x_{n_2}\in[a_2,b_2]$
	2. $n_2>n_1$
2. O caso 1 não vale. Então temos uma quantidade infinita de termos em $[\frac{a_1+b_1}{2},b_1]$. Então fazemos $a_2=\frac{a_1+b_1}{2}$,  $b_2 = b_1$ e $x_{n_2}$ tal que:
	1. $x_{n_2} \in [a_2,b_2]$
	2. $n_2>n_1$
Note que definimos $x_{n_k}$ a partir de $x_{n_{k-1}}$ usando esse raciocínio indutivamente. Então temos que $n_k>n_{k+1}$ pela construção e logo $x_{n_k}\in[a_k,b_k]$ tal que $a_k-b_k = \frac{b_{k-1} - a_{k-1}}{2}$. Mas como $I_1\supset I_2 \supset ...\supset$ temos que $b_k-a_k = \frac{b_{k-1}-a_{k-1}}{2^{k-1}}$. Pelo [[Teorema dos intervalos encaixados]] existe um único $l \in[a_k,b_k]$ para todo $k\in \mathbb{N}$. Então $|x_{n_k} -l| \leq (b_k-a_k) \leq (b_1-a_1)\frac{1}{2}^{k-1} < \epsilon$ para todo $k\geq K$ onde $K$ pode ser tão grande quanto quisermos. Assim $x_{n_k} \to l$ quando $K\to \infty$. $\Box$.  
