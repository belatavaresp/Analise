Seja $a_n \geq 0, (a_n)$ decrescente e $a_n \to 0\Rightarrow \sum (-1)^{n+1}a_n$ converge.
### Demonstração:
Vamos provar que existe $s \in \mathbb{R}$ tal que $s_{2n} \to s$ e $s_{2n-1}\to s$
1. $s_{2n+2} = s_{2n} + a_{2n+1} - a_{2n+2}$ como $a_{2n+1}-a_{2n+2} \geq 0 \Rightarrow s_{2n+2}\geq s_{2n}$ e portanto $(s_{2n})$ é crescente.
2. $s_{2n+1} = s_{2n-1} - a_{2n} + a_{2n+1}$ onde $a_{2n+1}-a_{2n} \leq 0$ e portanto $s_{2n+1}\leq s_{2n-1} \Rightarrow s_{2n-1}$ decresce.
3. $s_{2n} = s_{2n-1} -a_{2n} \Rightarrow s_{2n}\leq s_{2n-1}$
Logo, como $s_{2n}$ é limitada superiormente e é crescente $s_{2n} \to l_1$ e analogamente $s_{2n-1}\to l_2$, mas $l_1=l_2$ pois usando o item 3. e tirando o limite temos $lim \ s_{2n}  = lim \ s_{2n-1} -lim \ a_{2n} \Rightarrow l_1 = l_2 - 0 \Rightarrow l_1=l_2$
