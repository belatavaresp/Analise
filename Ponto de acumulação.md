Seja $X \subset \mathbb{R}$, $a\in\mathbb{R}$ é um ponto de acumulação de $X$ se $a = lim \ x_n$ onde $(x_n) \subset X\backslash\{a\}$.
#### Notação:
$X' =$ conjunto dos pontos de acumulação de $X$.

### Teorema 1:
Sejam $a \in \mathbb{R}$ e $X\subset \mathbb{R}: X \neq \emptyset$. As afirmações a seguir são equivalentes:

1. Para todo $\epsilon>0$, o conjunto $(a-\epsilon, a+\epsilon)\cap X\backslash\{a\} \neq \emptyset$
2. Existe $(x_n) \subset X \backslash \{a\}$ tal que $x_n \to a$
3. Para todo $\epsilon >0$ o conjunto $(a-\epsilon, a+\epsilon)\cap X\backslash\{a\}$ é infinito
#### Demonstração:
Primeiro vamos mostrar que $1\Rightarrow 2$.
Para cada $n\in\mathbb{N}$ definimos $\epsilon_n = \frac{1}{n}$ e $x_n \in (a-\epsilon_n, a+\epsilon_n)\cap X\backslash\{a\}$ (garantido pela hipótese). Então fica definida a sequência $(x_n)$ tal que $a-\frac{1}{n}<x_n<a+\frac{1}{n} \ \forall n \in \mathbb{N}$ que pelo [[Teorema do sanduíche]] sabemos que $x_n \to a$.

Agora vamos mostrar que $2 \Rightarrow 3$.
Seja $\epsilon >0$, como $x_n \to a$ existe $N\in\mathbb{N}$ tal que $\forall n\geq N$ temos que $|x_n-a|<\epsilon \iff x_n \in (a-\epsilon, a+\epsilon) \cap X \backslash\{a\}$ (pela hipótese). Então, sabemos que o conjunto dos termos de $x_n$ não pode ser finito, pois como ela é convergente isso implicaria que $x_n$ é constante a partir de algum índice, mas ela não contém $a$ logo, não pode ser finito.

