### Definição:
Um [[Corpo ordenado]] $\mathbb{K}$ é dito completo se todo $X \subseteq \mathbb{K}, X \neq \emptyset$ limitado superiormente tem [[Supremo]].

### Teorema 1:
$\mathbb{R}$ é um corpo ordenado completo.

### Teorema 2:
Se $\mathbb{K}$ é um corpo ordenado completo, então $\mathbb{K}$ é isomorfo à $\mathbb{R}$. 
#### OBS:
Se $X \subseteq \mathbb{R}, X\neq \emptyset$ e $X$ é limitado inferiormente $\Rightarrow$ $\exists \ inf(X)$.
**Dica da demonstração:**
Transformar $X \rightarrow Y:  Y = -X \Rightarrow \beta = \ sup(Y) \Rightarrow \alpha = -\beta \Rightarrow \alpha= \ inf(X)$.

### Teorema 3:
1. $\mathbb{N}$ não é limitado superiormente;
2. $inf\{\frac{1}{n} \  | \ n \in\mathbb{N}\} = 0$;
3. Para todos os $a,b \in \mathbb{R}^+$ (não inclui 0), existe $n \in \mathbb{N}$ tal que $na>b$. (Propriedade arquimediana de $\mathbb{R}$)
#### Demonstração:
Demonstraremos que $1\Rightarrow 2\Rightarrow 3\Rightarrow 1$. Primeiro mostremos 1:

1. Suponha que $\mathbb{N}$ é limitado superiormente $\iff$ existe $M \in\mathbb{R}$ tal que $n\leq M \ \forall n\in \mathbb{N}$. $\mathbb{R}$ é completo $\Rightarrow \exists S = \ sup(\mathbb{N})$. Logo $S-1$ não é [[Cota superior]] de $\mathbb{N}$ $\iff \exists n_0 \in \mathbb{N}$ tal que $n_0 > S-1\Rightarrow n_0+1 > S$ que é uma contradição pois $S$ é [[Supremo]] (e portanto cota superior) de $\mathbb{N}$. 
2. Sabemos que 0 é uma cota inferior. Vamos provar que $\forall c>0 \ \exists n\in \mathbb{N} : \frac{1}{n} < c$. Isso é equivalente a mostrar que dado um $c \ \exists n\in \mathbb{N}: n>\frac{1}{c}$. Porém por 1. sabemos que $\mathbb{N}$ não possui cota superior, logo sempre existe $n$ que satisfaz essa desigualdade. Assim sabemos que $0$ deve ser a maior das cotas superiores para o conjunto, pois caso contrário ele seria da forma de $c$.
3. Veja que $na>b \iff \frac{1}{n} < \frac{a}{b}$. Por 2. sabemos que que sempre existe $n\in \mathbb{N}: \frac{1}{n} < c$ então basta fazer $c=\frac{a}{b}$ para garantir que $\exists n: na>b$.
4. Fazendo $a=1$ em 3. obtemos exatamente o enunciado em 1.

### Teorema dos intervalos encaixados
Dada uma sequência de intervalos $I_n= [a_n, b_n]$ fechados, limitados e encaixados, ou seja: $I_1 \supset I_2 \supset ... \supset I_n \supset ...$ existe $c \in \mathbb{R}$ tal que $c\in I_n \ \forall n\in \mathbb{N}$. Note que $a_n \leq b_m \ \forall m,n \in \mathbb{N}$.
##### (Contra) Exemplos:
1. $I_n=(\sqrt{2}, \sqrt{2}+\frac{1}{n})$. Sabemos que podemos chegar infinitamente perto de $\sqrt{2}+\frac{1}{n}$, então temos que a interseção de todos os $I_n: n\rightarrow \infty = \emptyset$. Logo nota-se que é importante a hipótese de que os intervalos encaixados sejam fechados.
2. $I_n = [n,+\infty)$. Se existisse $c \in I_n: c\geq n \ \forall n \in \mathbb{N}$, mas sabemos que $\mathbb{N}$ não é limitado superiormente, portanto a interseção desses intervalos encaixados também é vazia mostrando que é necessária a hipótese de que eles sejam limitados para que valha o teorema.
#### Demonstração:
Seja $X = \{a_n \ | \ n\in \mathbb{N}\} \neq \emptyset$, ele é limitado superiormente pois sabemos que $a_n \leq b_1 \ \forall n\in \mathbb{N}$. Seja $c=sup(X)$ e portanto $a_n \leq c \ \forall n\in\mathbb{N}$. Como $b_m$ é cota superior de $X$ para todo $m\in\mathbb{N}$, temos que $c \leq b_m \ \forall m\in\mathbb{N}$ logo $c \in I_n$para qualquer $n\in\mathbb{N}$. (Consequência direta de $\mathbb{R}$ ser completo).