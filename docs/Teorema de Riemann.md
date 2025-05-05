Se a [[Série numérica]] $\sum a_n$ é condicionalmente convergente (converge mas não é uma [[Série absolutamente convergente]]) então para todo $c \in \mathbb{R}$ existe $\phi: \mathbb{N}\to\mathbb{N}$ tal que $\sum a_{\phi(n)}$ converge e sua soma é $c$.

### Consequência:
- Prova a recíproca do [[Comutatividade#Teorema 1]]

##### OBS:
Se $\sum a_n$ é condicionalmente convergente então $\sum a_n^+$ ou $\sum a_n^-$ diverge. Mas, se $s_n = a_1+...a_n$ então $s_n = (a_1^++...+a_n^+)-(a_1^-+...+a_n^-)$, porém, como $\sum a_n$ é convergente então as duas séries, $\sum a_n^+$ e $\sum a_n^-$, precisam divergir. 

### Demonstração:
Seja $(n_k)$ a sequência dos índices dos termos positivos de $a_n$ e $(m_l)$ a sequência dos índices dos termos negativos.

**Passo 1:** 
Faça $\tilde{s}_k = a_{n_1}+...+a_{n_k} > c$ onde $a_{n_1}+...+a_{n_{k-1}} \leq c$. Note que $\tilde{s}_k -c < a_{n_k}$ e $\tilde{s}_k > c$. Então, temos definidas as primeiras $k$ somas parciais, ou seja, os primeiros $k$ termos na nossa reordenação.

**Passo 2:**
Faça $\tilde{s}_{k+l-1} + a_{m_1}+ ... +a_{m_{l-1}} \geq c$ e $\tilde{s}_{k+l} + a_{m_1}+...+a_{m_l} < c$. Note que $c-\tilde{s}_{k+l} < a_{m_l}$.

%% Falta terminar, provar que vale a definição de limite dado epsilon %%
