### Definição:
Seja $X$ um conjunto. Se $X = \emptyset$ ou $\exists n \in \mathbb{N}$ tal que existe $\phi: I_n \rightarrow X$ bijeção, então dizemos que $X$ é finito.
##### Obs 1:
$n$ = cardinalidade ou número cardinal de $X$.
##### Obs 2:
$\phi$ é uma enumeração de $X$.

#### Lema 1:
Seja $f: X \rightarrow Y$ uma bijeção e seja $x_0 \in X$ e $y_0 \in Y$, então existe $\tilde{f}: X \rightarrow Y$ bijeção tal que $\tilde{f}(x_0)=y_0$.

### Teorema 1:
Se para algum $n \in \mathbb{N}$, $A\subset I_n$ (subconjunto próprio), então não há nenhuma bijeção $f: A \rightarrow I_n$. 
##### Demonstração:
Vamos supor que a conclusão é falsa. Então seja $Z = \{n \in \mathbb{N} \ | \ \text{existem} \ A \subset I_n \ \text{e} \ f: A\rightarrow I_n \ \text{bijeção}\}$ e $Z \neq \emptyset$. Seja $n_0 = min \ Z$, $A$ tal que $A \subseteq I_{n_0}$, $f: A \rightarrow I_{n_0}$ é bijeção.
	Caso 1: $n_0 \in A$.  Seja $\tilde{f}: A \rightarrow I_{n_0}$ bijeção tal que $\tilde{f}(n_0) = n_0 \Rightarrow \tilde{f}|_{A\backslash \{n_0\}} \rightarrow I_{n_0 -1}$ bijeção pelo [[Conjunto finito#Lema 1]], que é uma contradição com a minimalidade do $n_0$.
	Caso 2: $n_0 \notin A$. Seja $f: A\rightarrow I_{n_0}$ bijeção. $\Box$ 
###### OBS: 
Se $X$ é finito e $f: X \rightarrow Y$ é bijeção $\Rightarrow$ $Y$ é finito.

#### Corolário 1
Vale o mesmo para $I_n = X$ conjunto finito. 
##### Demonstração (ideia):
Assume que existe, usa a definição de $X$ finito e acha uma contradição com o Teorema 1.

#### Corolário 2
Seja $X$ um conjunto finito e $f: X \rightarrow X$. Então $f$ é injetiva $\iff f$ é sobrejetiva.
##### Demonstração:
(Ida) Se $f$ é injetiva, considere $f: X \rightarrow f(X)$ é bijeção $\Rightarrow f(X) = X$.
(Volta) %% Exercício %% 
##### Exemplos:
1. $X = \{1, 2\} \ \ \ f(1)=f(2)=1$
2. *(Contraexemplo para conjuntos infinitos)* $f : \mathbb{N} \rightarrow \mathbb{N}$ definida por $f(n) = 2n$ é injetiva mas sua imagem são apenas os naturais pares, ou seja, não é sobrejetiva, portanto $\mathbb{N}$ não é finito. 

### Teorema 2:
Se $X$ é finito e $Y \subseteq X \Rightarrow Y$ é finito.
##### Demonstração:
Vamos demonstrar por [[Indução]] no tamanho de $X$.
1. Base: $X = \emptyset,\ Y \subseteq X \Rightarrow Y = \emptyset$ e portanto finito.
2. Hipótese de indução: Assumimos $|X| = n, \ Y\subseteq X \Rightarrow Y$ é finito.
   Passo indutivo: Seja $|X| = n+1, \ Y\subseteq X$ temos dois casos possíveis:
	1. $Y = X \Rightarrow Y$ finito.
	2. $Y\subset X \Rightarrow \exists a \in X: a\notin Y$, logo pela hipótese, $Y$ é finito. $\Box$ 
#### Lema 2:
Seja $X$ finito e $a\in X \Rightarrow X \backslash \{a\}$ é finito.
##### Demonstração:
1. $|X| = 1 \Rightarrow X\backslash \{a\} = \emptyset$ que é finito.
2. $|X| = n > 1$. Seja $\phi :  I_n \rightarrow X$ bijeção tal que $\phi (n) = a$ *(garantido pelo [[Conjunto finito#Lema 1]])*. Então $\phi |_{I_{n-1}}: I_{n-1} \rightarrow X \backslash \{a\}$ é uma bijeção e logo $X\backslash\{a\}$ é finito. $\Box$ 

#### Corolário 1:
Um conjunto $X \subseteq \mathbb{N}$ é finito $\iff$ é limitado