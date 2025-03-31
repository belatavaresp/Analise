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


