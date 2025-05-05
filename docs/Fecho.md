## Ponto de aderência
$x_0\in \mathbb{R}$ é ponto de aderência de $X\subset \mathbb{R}$ se existe $(a_n)\subset X$ tal que $a_n \to x_0$ 

##### OBS:
$x_0 \in X \Rightarrow x_0$ é ponto de aderência de $X$.

## Fecho
O fecho de $X$ ($\bar{X}$) é o conjunto de todos os pontos de aderência de $X$
##### OBS:
- $X \subset \bar{X}$
- $X \subset Y \Rightarrow \bar{X} \subset \bar{Y}$ 

### Teorema 1 (Caracterização dos pontos de aderência)
$a \in \mathbb{R}$ é [[Fecho#Ponto de aderência]] de $X \iff \ \forall \epsilon>0 \ (a-\epsilon, a+\epsilon)\cap X \neq \emptyset$
#### Demonstração:
1. ($\Rightarrow$) Seja $(x_n) \subset X$ tal que $x_n \to a$ e seja $\epsilon>0$ existe $N\in\mathbb{N}$ tal que $x_N \in (a-\epsilon, a+\epsilon) \Rightarrow x_N \in X \cap (a-\epsilon, a+\epsilon)$.
2. ($\Leftarrow$) Faça $\epsilon = \frac{1}{n}$. Para todo $n \in \mathbb{N}$ seja $x_n \in (a-\frac{1}{n}, a+\frac{1}{n})\cap X$, mas então $a-\frac{1}{n} < x_n < a+\frac{1}{n}$ e pelo [[Teorema do sanduíche]] $x_n \to a$.
#### Corolário 1:
$\bar{\bar{X}} = \bar{X}$, ou seja o fecho de $X$ é [[Fechado]]
##### Demonstração:
Vamos provar que $\bar{\bar{X}}\subset \bar{X}$.
**OBS:** Podemos trocar $(a-\epsilon,a+\epsilon), \epsilon>0$ por qualquer [[Aberto]] contendo $a$ $\iff$ todo $A$ [[Aberto]] tal que $a\in A$ satisfaz $A\cap X \neq \emptyset$ (o que sabemos ser verdade pelo Teorema 1).
Seja $a\in \bar{\bar{X}}$ e seja $A$ aberto, se $a\in A$ então $A\cap\bar{X}\neq \emptyset$. Seja $b \in A\cap\bar{X}$ pelo mesmo motivo podemos aplicar o Teorema 1 novamente e concluir que $A \cap X \neq \emptyset \Rightarrow a \in \bar{X}$.
