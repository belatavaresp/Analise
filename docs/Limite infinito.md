### Definição:
$x_n\to \infty (-\infty) \iff$ para todo $A>0$ existe $N\in \mathbb{N}$ tal que $n\geq N \Rightarrow x_n >A (x_n<A)$ 
##### OBS:
1. $x_n \to \infty \iff -x_n \to -\infty$ 
2. $\pm \infty$ não são números, $x_n \to \pm \infty \Rightarrow (x_n)$ diverge.

### Exemplos:
1. $x_n = n, x_n \to \infty$
2. $x_n = a^n, a>1$
3. $k\in \mathbb{N}, a>1$

### Propriedades:
1. $x_n \to +\infty, x_n\leq y_n, n\geq N \Rightarrow y_n \to +\infty$
2. $x_n \to +\infty \Rightarrow x_n$ é ilimitada superiormente (não vale a volta)
3. $x_n$ crescente e ilimitada superiormente $\Rightarrow x_n \to +\infty$
4. $x_n \to +\infty,  y_n > c, n\geq 1, c\in \mathbb{R} \Rightarrow x_n+y_n \to +\infty$.
	**Prova:**
	Seja $A>0$. Existe $N_1 \in \mathbb{N}$ tal que $n\geq N_1 \Rightarrow x_n > A-c$. Seja $N_2 = max\{N, N_1\}$ então se $n\geq N_2$, temos $y_n>c, x_n > A-c \Rightarrow x_n+y_n > A \ \Box$.
5. $x_n \to +\infty, y_n > c > 0, n\geq 1 \Rightarrow x_ny_n\to +\infty$ %% Exercício provar %%
6. $z_n >0, z_n \to 0, y_n>c>0, n\geq N \Rightarrow \frac{y_n}{z_n}\to \infty$ %% Exercício (provar que $x_n = \frac{1}{z_n}$) %% 
7. $y_n \to +\infty, x_n$ limitada $\Rightarrow \frac{x_n}{y_n}\to 0$ %% Exercício provar %%