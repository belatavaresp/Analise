Seja um conjunto $X \subset \mathbb{R}$, $X$ é aberto se é igual ao seu [[Interior]], ou seja $X = int \ X$.
### Exemplos:
1. $(a,b)$ 
2. $[a,+\infty]$ não é aberto
3. $int \ \mathbb{Q} = \emptyset \neq \mathbb{Q}$ 
4. $\emptyset$ é aberto
5. $\mathbb{R}$ é aberto

### Teorema 1:
Sejam $A_1, A_2$ abertos então:

- $A_1 \cap A_2$ é aberto
- $\{A_\lambda| \lambda \in \Lambda\}$ abertos $\Rightarrow \bigcup_{\lambda \in \Lambda}{A_\lambda}$ é aberto
#### Demonstração:
1. Se $x \in X_1$ então existe $\epsilon_1>0$ tal que $(x-\epsilon_1, x+\epsilon) \subset A_1$. 
	Se $x\in X_2$ então existe $\epsilon_2>0$ tal que $(x-\epsilon_2,x+\epsilon_2)\subset A_2$
	Faça $\epsilon = min \{\epsilon_1,\epsilon_2\} \Rightarrow (x-\epsilon, x+\epsilon) \subset A_1 \cap A_2$ 
2. Seja $x \in \bigcup_{\lambda \in \Lambda}{A_\lambda}$ então existe $\lambda \in \Lambda$ tal que $x \in A_\lambda$. $A_\lambda$ aberto e portanto existe $\epsilon>0$ tal que $(x-\epsilon, x+\epsilon) \subset A_\lambda \subset \bigcup_{\lambda \in \Lambda}{A_\lambda}$. 

##### OBS:
- A interseção (finita) de $n$ abertos também é aberta e pode ser demonstrado por indução.
- A união do caso 2 pode ser finita, enumerável ou não enumerável, mas continua valendo que é aberta.
