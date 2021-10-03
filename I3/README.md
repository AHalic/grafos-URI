# Exercícios do URI - Dijkstra e Ford-Fulkerson

## Exercício 1362
Os algoritmos usados foram os de Ford-Fulkerson e Dijkstra. O grafo que descreve o exercício tem um vértice sumidouro e um fonte, 6 vértices sendo cada um dos 6 tamanhos de blusa (XS, S, M, L, XL, XXL) e mais n vértices sendo cada um um voluntário.

O vértice fonte possui uma aresta para cada voluntário, que por sua vez possui uma aresta para cada respectivo tamanho de blusa. Por fim cada tamanho de blusa possui uma aresta para o vértice sumidouro.
    
O algoritmo de Ford-Fulkerson foi usado para encontrar o fluxo máximo do grafo, que por sua vez seria utilizado para comparar se era igual a quantidade de voluntários. Caso o fluxo máximo fosse menor, isso indicaria que não foi possível todos os voluntários conseguirem blusas. 

Os melhores tempos obtidos para este exercício foram 1.052s com Python 3.8 (ranking Sophie Dilhon, posição 31) e  1.229s Python 3.9 (ranking Beatriz Maia, posição 34).

## Dijkstra
O algoritmo foi usado para encontrar o menor caminho de um vértice para todos os outros, sendo esse o corte utilizado no algoritmo de Ford-Fulkerson. O algoritmo para de rodar até que se encontre o vértice sumidouro t, isso pois os próximos caminhos não importam para a questão (mesmo que alguns vértices não tenham sido encontrados ainda).

## Ford-Fulkerson
Utilizando Dijkstra para encontrar o corte, percorremos o grafo até que não haja conexão entre a fonte e o sumidouro. O fluxo mínimo do corte sempre será igual a 1 dado a relação criada pelo nosso grafo, entre a origem e os voluntários e dos voluntários para as blusas (o peso destas arestas sempre são 1). Como conhecemos o fluxo mínimo anteriormente, não adicionamos ao programa o loop necessário para encontrá-lo, visando a otimização do nosso código. 
