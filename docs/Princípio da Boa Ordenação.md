Seja $A \subset \mathbb{N}: A\neq \emptyset$ então A tem um elemento mínimo, ou seja, $\exists n_0 \in A: n\geq n_0 \ \ \forall n \in A$.

**Demonstração:**
- Caso 1: $1\in A$, então 1 é um mínimo de A.
- Caso 2: $1 \notin A$. Seja $I_n = \{m \in \mathbb{N}: m \leq n\}$ e $X = \{n \in \mathbb{N}: I_n \subset A^c\}$.
	a) Note que $1\in X$ por que $I_1$ não está em A.
	b) Sabemos que como $A \neq \emptyset$ então $s(X)\not \subset X$, assim pelo [[Indução]], $X \neq \mathbb{N}$, logo $\exists n \in X$ tal que $n+1 \notin X$, então $n+1 \in A$ e portanto é um mínimo.