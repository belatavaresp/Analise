### Definição
Seja $X$ um conjunto. Dizemos que $X$ é enumerável se:
1. $X$ é finito ou;
2. Existe $\phi: \mathbb{N} \rightarrow X$ bijeção.
#### Exemplos
1. $\mathbb{N}$
2. $2\mathbb{N}, \phi(n) = 2n$
3. $X$ = conjunto dos primos
4. $\mathbb{Z}, \phi(n) = \begin{cases} \frac{-n}{2}, & \text{se } n \text{ é par} \\ \frac{n-1}{2}, & \text{se } n \text{ é ímpar} \end{cases}$  %% Exercício: provar a bijeção %%

Pelo [[Conjunto infinito#Teorema 1]] sabemos que existe $\phi: \mathbb{N} \rightarrow X$ injetiva, mas note que $\phi: \mathbb{N} \rightarrow \phi(\mathbb{N})$ é uma bijeção, então $\phi(\mathbb{N}) \subseteq X$ é enumerável, assim concluímos:

### Teorema 1:
Todo conjunto infinito possui um subconjunto enumerável.
#### Corolário 1:
Se $X$ é enumerável e existe $f: X \rightarrow Y$ bijeção, então $Y$ também é enumerável.

### Teorema 2:
$X \subseteq \mathbb{N} \Rightarrow X$ é enumerável.
##### Demonstração:
- Caso 1: $X$ é finito $\rightarrow$ Ok!
- Caso 2: $X$ é infinito.
	Seja $x_1 = min \ X$ (existe pelo [[Princípio da Boa Ordenação]]), $x_2 = min \ X\backslash \{x_1\}$ e assim por diante até $x_{n+1} = min \ X \backslash \{x_1, ..., x_{n}\}$. Seja $\phi: \mathbb{N} \rightarrow X$ definida dessa forma, sabemos que ela é injetiva. Precisamos provar que $X = \{x_1, x_2, ..., x_n, ...\}$. Suponha que existe um elemento $a \in X\backslash \{x_1,x_2,...\}$, sabemos que $a \geq x_n \ \forall n\in \mathbb{N}$ pela construção da sequência e portanto ela é limitada superiormente por $a$ o que implicaria que $X$ é finito pelo [[Conjunto finito#Corolário 1]], um absurdo. 
#### Corolário 2:
Seja $f: X \rightarrow Y$ e $Y$ enumerável $\Rightarrow X$ é enumerável.
##### Demonstração:
$\exists \ \phi: \mathbb{N} \rightarrow Y$ bijetiva, então $f: X \rightarrow f(X) \subseteq Y$ é bijetiva e portanto $\tilde{\phi}: A \subseteq \mathbb{N} \rightarrow f(X)$ é bijetiva. Assim encontramos $\psi: A\subseteq \mathbb{N} \rightarrow X$ bijeção e pelo [[Enumerável#Corolário 1]] $X$ é enumerável.
#### Corolário 3:
Seja $f: X \rightarrow Y$ sobrejetiva e $X$ enumerável $\Rightarrow Y$ é enumerável.
#### Corolário 4:
Sejam $X, Y$ conjuntos enumeráveis $\Rightarrow X \times Y$ é enumerável.
