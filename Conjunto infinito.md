### Definição:
Um conjunto que não possui enumeração, ou seja não é um [[Conjunto finito]].

#### Lema 1:
Seja $X$ infinito, então $\exists Y\subset X$  infinito.
##### Demonstração:
Seja $a \in X$ e defina $Y = X\backslash\{a\}$. Se $Y$ é finito, então existe uma bijeção $\phi$ de $Y$ com $I_n$ para algum $n\in \mathbb{N}$, mas então podemos definir $\tilde{\phi}(m) =\begin{cases} \phi(m), & m \in I_n \\ a, & m = n+1\end{cases}$ o que implicaria $X$ finito, absurdo. $\Box$ 
### Teorema 1:
Se $X$ é infinito, $\exists \phi: \mathbb{N} \rightarrow X$ injetiva.
##### Demonstração:
Vamos demonstrar usando um raciocínio de [[Indução]]. Seja $\phi(1) = x_1$ (qualquer elemento de $X$). Seja $x_2 \in X \backslash \{x_1\}$ definimos $\phi(2) = x_2$, e assim em diante até $\phi(n)$. Então $\phi(n+1) = x_{n+1} \in X \backslash \{x_1,x_2,...,x_n\}$ e assim $\phi: \mathbb{N} \rightarrow X$ está bem definida e é injetiva.
Pois, sejam $n<m$ ($n\leq m-1$), $\phi(m) \in X \backslash \{\phi(1), ..., \phi(m-1)\}$ e $\phi(n) \in X \backslash \{\phi(1), ..., \phi(m-1)\} \Rightarrow \phi(m) \neq \phi(n)$. $\Box$ 

#### Corolário 1:
Se $X$ é infinito, existe $Y \subset X$ e $\phi: X \rightarrow Y$ bijeção.
##### Exemplos:
1. $\phi : \mathbb{N} \rightarrow 2\mathbb{N}: \phi(n)=2n$;
2. $\phi: \mathbb{N} \rightarrow \mathbb{N} \backslash \{1\}: \phi(n) = n+1$.
