# Exercícios do URI - Árvores Geradoras

Por os exercícios apresentarem uma lógica similar, a escolha do algoritmo para cada exercício foi aleatória. Ambos os exercícios recebiam como entrada um grafo e tinham como saída a menor soma de suas arestas. Optamos por deixar os pseudocódigos dos algoritmos em cada executável para auxiliar a sua construção.

## Algoritmo de Prim - Exercício 1774

Para encontrar o menor custo de cabos é necessário encontrar a MST, foi usado o algoritmo de Prim para isso. 

Para o algoritmo, é necessário inicializar um vetor de pesos com valores muito grandes. Esse vetor representa o custo para se alcançar cada vértice (de mesmo valor que o índice) em relação a MST. Para forçar que o primeiro nó encontrado no loop seja o de índice zero, o peso deste é modificado no vetor de pesos para zero.

O primeiro loop do algoritmo roda até que a MST contenha a mesma quantidade de nós do grafo original. 
Por otimização do código não são salvas as arestas da MST, apenas seus custos, uma vez que a questão demanda apenas o menor custo para os cabos.

O melhor tempo foi em 0.009 em Python 3.8 (Beatriz Maia) e o pior tempo 0.037s em Python 3.4 (Sophie Dilhon).
 
## Algoritmo de Kruskal - Exercício 2404

Para encontrar a menor soma do comprimento das rodovias que passavam por todas cidades, foi utilizado o algoritmo de Kruskal para isso. 

A estrutura utilizada foi de uma lista de dicionário, em que cada item representava uma aresta. Apesar do grafo não ser direcionado, por simplicidade dos termos, escolhemos os nomes das chaves do dicionário "origin" e "destiny". 

Na função de `kruskal`, há dois valores inicializados inicialmente: `tree_size` e `cost`. Observa-se que há comentada uma lista `tree`, isso é devido ao fato que o algoritmo adiciona as arestas a uma MST, porém para a resolução do exercício, não houve necessidade de acessar o conteúdo dessa árvore. Em vez disso, é utilizada uma lista (`parents`) que atua como árvore, a partir da estrutura de Union-Find . A variável `tree_size` contabiliza a quantidade de arestas na árvore. No while, é verificado se a aresta tornaria o grafo cíclicio através da função `find`, ao verificar a raíz absoluta dos vértices que se deseja conectar (caso tenham mesma raíz então seria cíclico). Quando é adicionada uma aresta na árvore, é utilizada a função `union`. A variável `cost` armazena o peso das arestas adicionadas. 

O melhor tempo no URI foi de 0.325 em Python 3.9
(Beatriz Maia) e o pior 0.336s em Python 3.8 (Sophie Dilhon).


