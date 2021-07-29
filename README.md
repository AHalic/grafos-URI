# Exercícios do URI

## Busca em profundidade - Exercício 1082 
Estado: OK

Para verificar a quantidade de componentes conexas, reaproveitamos a representação de grafo em lista da EA1 e modificamos alguns métodos. Como o grafo sempre será não direcionado e não valorado, retiramos estes métodos e simplificamos a classe grafo. 

Os melhores tempos obtidos para este exercício foram 0.335s com Python 3.8 (ranking Sophie Dilhon) e 0.213s com Python 3.8 (ranking Beatriz Maia). 

## Busca em largura - Exercício 1550
Estado: OK

Para calcular a quantidade mínima de apertos de botão, o algoritmo vai gerando uma árvore enquanto a percorre por amplitude. Para cada vértice visitado, é gerado dois novos vértices: o valor do vértice invertido e valor do vértice incrementado.  

Os melhores tempos obtidos para este exercício foram 2.640s com Python 3 (ranking Sophie Dilhon) e 2.788s com Python 3.8 (ranking Beatriz Maia). 

Para a escolha das estruturas utilizamos como pesquisa [este link](https://wiki.python.org/moin/TimeComplexity). De início estavamos utilizando apenas listas, porém isso resultou em excedendo o tempo. Após a modificação de lista para conjunto, conseguímos diminuir consideravalmente o tempo. Isso era devido a utilizarmos o comando `if {vertice} not in historico`, sendo vértice ou a variável soma ou a variável invertido. Além disso, para diminuir o tempo também retiramos o `if __name__ == "__main__"` dado o fato que em alguns casos isso mostrava a adicionar tempo. 