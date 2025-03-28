### Definição
Um conjunto não vazio $\mathbb{K}$ é um **corpo** se em $\mathbb{K}$ pudermos definir 2 operações, denotadas por adição ($+$) e multiplicação ($\cdot$) satisfazendo as propriedades:
#### Axiomas da adição
- **A1**: $a+b=b+a , \ \ \forall a,b \in \mathbb{K}$  (propriedade comutativa).
- **A2**: $a+(b+c) = (a+b)+c, \ \ \forall a,b,c \in \mathbb{K}$  (propriedade associativa).
- **A3**: Existe um elemento em $\mathbb{K}$ denotado por 0 e chamado de *elemento neutro* da adição que satisfaz $0+a = a+0 = a, \ \ \forall a \in \mathbb{K}$.
- **A4**: Para cada $a \in \mathbb{K}$ existe um elemento em $\mathbb{K}$ denotado por $-a$ e chamado de *oposto de a* ou *inverso aditivo de a* tal que $a + (-a) = (-a) + a = 0$.
#### Axiomas da multiplicação
- **M1**: $a \cdot b = b \cdot a, \ \ \forall a,b,c \in \mathbb{K}$  (propriedade comutativa).
- **M2**: $a \cdot (b \cdot c) = (a \cdot b) \cdot c, \ \ \forall a,b,c \in \mathbb{K}$  (propriedade associativa).
- **M3**: Existe um elemento em $\mathbb{K}$, denotado por 1 e chamado de *elemento neutro da multiplicação*, tal que $1\cdot a = a \cdot 1, \ \ \forall a \in \mathbb{K}$.
- **M4**: **Para cada** elemento não nulo $a \in \mathbb{K}$, existe um elemento em $\mathbb{K}$, denotado por $a^{-1}$ e chamado de *inverso multiplicativo de a*, tal que $a \cdot a^{-1} = a^{-1} \cdot a = 1$.
#### Lei distributiva
- **D**: $(a+b) \cdot c = a \cdot c + b \cdot c, \ \ \forall a,b,c \in \mathbb{K}$  (propriedade distributiva).

### Exemplos:
1. $\mathbb{Q}, \mathbb{Z}_2, \mathbb{R}$ são corpos
2. $\mathbb{N}$ não é corpo pois falha no **A4**
3. $\mathbb{Z}$ não é corpo pois falha no **M4**

### Proposição 1.1
1.  Sejam $x, y, z \in \mathbb{K}$, $x+y = x+z \Rightarrow y = z$ 
	**Demonstração:**
	Pelo axioma **A4** temos $(x+y) + (-x) = (x+z)+(-x) \Rightarrow x+y-x=x+z-x$ pelo axioma **A2** então $x-x+y=x-x+z \Rightarrow 0+y=0+z$ pelo axioma **A2** e por fim $y=z$ pelo axioma **A3** $\Box$.
2. Seja $x\in \mathbb{K}, -(-x) = x$ 
	**Demonstração:**
	Pela definição de oposto $-(-x) = -x+x$, pelos axiomas **A1** e **A4** $-x+x = x-x = 0$ 
3. Sejam $x,y \in \mathbb{K}, (-x)y = -(xy)$ 
	**Demonstração:** %%Exercício%%
4. Seja $x \in\mathbb{K}$, $x\cdot 0=0 \ \forall x$.
	**Demonstração**:
	Sabemos que por **A4** $0 = 1-1$. Então por **D** e por 3) $x(1-1)= x(1)+x(-1) = x-x = 0$.
### Proposição 2.2
1. Seja $x,y \in \mathbb{K}$ tais que $x\neq0, y\neq0 \Rightarrow xy\neq0$. Analogamente, $xy = 0 \Rightarrow x = 0 \lor y=0$.
	**Demonstração:**
	Suponha $xy = 0$. O axioma **M4** garante que $x^{-1}xy= x^{-1}\cdot0$ e por **M4, M3** e **M1** $y = 0$ que é absurdo pois assumimos $x\neq 0, y\neq 0$.
