### Definição:
A [[Sequência]] $(x_n)$ tem limite $l\in \mathbb{R}$ se para todo $\epsilon >0$, existe $N \in \mathbb{N}$ tal que $n\geq N \Rightarrow |x_n-l|<\epsilon$ ou seja, $x_n \in V_{\epsilon}(l)$, que é a [[Vizinhança]] de raio $\epsilon$ ao redor do limite.

#### Notação:
$x_n \rightarrow l \iff x_n\rightarrow l, n\rightarrow \infty \iff \lim_{n \to \infty} x_n = l$. 
Uma sequência $(x_n)$ pode ser convergente, se possui limite, e divergente se não o possui.

### Teorema 1 (Unicidade):
Uma sequência não pode convergir para dois limites distintos.
#### Demonstração:
Suponha $x_n \to l$ e seja $b\neq l$. Seja $\epsilon > 0$ tal que $(l-\epsilon, l+\epsilon) \cap (b-\epsilon, b+\epsilon) = \emptyset$. Pela definição, existe $N_{\epsilon} \in \mathbb{N}$ tal que $x_n \in (l-\epsilon, l+\epsilon)$ para todo $n\geq N_{\epsilon}$. Portanto a vizinhança $V_{\epsilon}(b) = (b-\epsilon, b+\epsilon)$ pode conter uma quantidade finita de termos de $(X_n)$ concluímos então que $X_n \not \to b$. $\Box$.