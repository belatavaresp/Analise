$X$ é fechado se $X = \bar{X}$ ou seja se $X$ é igual ao seu [[Fecho]]
##### OBS:
- $X$ é fechado$\iff \bar{X}\subset X$ (basta mostrar isso para concluir)
### Exemplos:
1. No conjunto $X = \{1,2,3\}$, $\bar{X} = X$, logo $X$ é fechado
2. No conjunto $X = [a,b]$, $\bar{X} = X$, logo $X$ é fechado
3. No conjunto $X = (a,b)$, $\bar{X} = [a,b]$ (Vale para aberto em só um dos lados) como $\bar{X}\not \subset X$ então $X$ não é fechado.
4. $\emptyset$ é fechado
5. $\mathbb{R}$ é fechado.

### Teorema 1:
$X$ é fechado $\iff X^c$ é [[Aberto]].
#### Demonstração:
($\Rightarrow$) Seja $a\in X^c$, ou seja $a \notin X \iff$ a não é [[Fecho#Ponto de aderência]] de $X$, então pelo [[Fecho#Teorema 1 (Caracterização dos pontos de aderência)]] $\exists \epsilon_0 > 0$ tal que $(a-\epsilon_0,a+\epsilon_0)\cap X = \emptyset \iff (a-\epsilon_0, a+\epsilon_0)\subset X^c \iff X^c$ é [[Aberto]].

($\Leftarrow$) Basta provar que $\bar{X} \subset X$. Seja $a \in \mathbb{R}$ um ponto de aderência de $X$ e seja $\epsilon>0$, então $(a-\epsilon,a+\epsilon)\cap X \neq \emptyset$, mas nenhuma vizinhança simétrica de $a$ pode estar contida em $X^c$ então como $X^c$ é aberto temos que $a \in X$.

### Teorema 2
Sejam $F_1, F_2$ conjuntos fechados:

- $F_1\cup F_2$ é fechado
- $\{F_\lambda|\lambda \in \Lambda\}$ fechados $\Rightarrow \bigcap_{\lambda \in \Lambda}F_\lambda$ é fechado
#### Demonstração:
Vamos usar o [[Aberto#Teorema 1]] em conjunto com o Teorema 1 acima.

1. $(F_1\cup F_2)^c = F_1^c \cap F_2^c$ é aberto logo $F_1 \cup F_2$ é fechado.
2. $[\bigcap_{\lambda \in \Lambda}F_\lambda]^c = \bigcup_{\lambda \in \Lambda}F_\lambda^c$ é aberto logo $\bigcap_{\lambda \in \Lambda}F_\lambda$ é fechado.

##### OBS:
- $\{x\}$ é fechado.
- $X = \bigcup_{x \in X}\{x\}$ não necessariamente é fechado (pois senão união não enumerável seria fechada).
