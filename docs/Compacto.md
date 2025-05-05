$X \subset \mathbb{R}$ é compacto de se for [[Fechado]] e limitado.

#### Exemplos de compactos:
1. $X = [a,b]$
2. $X$ finito
#### Exemplos de não compactos:
1. $X = (a, b], (a,b), (a,+\infty)$
2. $X = \mathbb{Z}$

##### OBS:
$X$ é [[Fechado]] $\iff$ se $(x_n) \subset X: x_n \to a \Rightarrow a \in X$

### Teorema 1:
$X \subset \mathbb{R}$ é compacto se e somente se toda sequência de elementos de $X$ possui alguma subsequência convergente para um elemento de $X$.
#### Demonstração:
$(\Rightarrow)$ Seja $X$ fechado e limitado e $(x_n) \subset X$.
1. Pelo [[Teorema de Bolzano-Weierstrass para conjuntos]] existe $x_{n_k} \to a \in \mathbb{R}$
2. Como $X$ é fechado $\Rightarrow a \in X$.
($\Leftarrow$) Suponha que $X$ não seja limitado, então existe $(x_n) \subset X$ tal que $|x_n|>n \ \forall n \in \mathbb{N}$ e logo nenhuma subsequência poderia convergir (absurdo), portanto $X$ é limitado. Agora, mostremos que $X$ é fechado. Seja $(x_n) \subset X : x_n \to a$. Existe subsequência de $x_n$ que converge para $a^* \in X$ logo $a = a^* \Rightarrow a \in X \Rightarrow X$ é fechado (pela OBS).

### Teorema 2:
Se $X \subset \mathbb{R} : X \neq \emptyset$ então existem $\alpha = min \ X$ e $\beta = max \ X$.
#### Demonstração:
1. $X$ é limitado $\Rightarrow \alpha = inf \ X, \beta = sup \ X$
2. $X$ é fechado $\Rightarrow$ temos uma sequência de elementos de $X$ que converge para o [[Ínfimo]] e outra que converge para o [[Supremo]] então $\alpha$ e $\beta$ são [[Fecho#Ponto de aderência]] e portanto pertencem a $X$.