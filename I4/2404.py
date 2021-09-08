'''
Algoritmo de Kruskal 

Entrada: G = (V,E), Lista de Adjacência de G: A(v), v E V,
matriz de pesos
1. ordenar as arestas e de G pelo valor de seus pesos
2. T ← vazio;
3. para-todo i = 1, ..., |E| faça
4.      se T U {e} é acíclico então
5.          T ← T U {e};
6.      fim-se
7. fim-para-todo;
saída: T
'''

def read_graph():
    nodes, edges = map(int, input().split())

    # Cria grafo vazio
    graph = []
    for _ in range(edges):
        origin, destiny, weight = map(int, input().split())
        graph.append({
            'origin': origin,
            'destiny': destiny,
            'weight': weight,
            'connected': False
        })
        
    return graph, nodes, edges

def kruskal(graph, nodes, edges):

    sorted_graph = sorted(graph, key = lambda k: k['weight'])
    tree = set()
    cost = 0
    # print(*sorted(graph, sep="\n"))
    for edge in sorted_graph:
        print("arvore", tree)
        print("detino", edge['destiny'])
        print("origem", edge['origin'])
        # não consegue ligar componentes conexas
        if cost == 0 or (edge['destiny'] in tree and edge['origin'] not in tree) or (edge['destiny'] not in tree and edge['origin'] in tree):
            tree.add(edge['destiny'])
            tree.add(edge['origin'])
            edge['connected'] = True
            cost += edge['weight']
        # CAGUEI O CODIGO
        elif edge['destiny'] not in tree and edge['origin'] not in tree:
            print("adicionei a aresta")
            tree.add(edge['destiny'])
            tree.add(edge['origin'])
            cost += edge['weight']


        else:
            for i in range(edges):
                aux_edge = sorted_graph[i]
                if not edge['connected']:
                # Ver se as edges que estão no grafo fazem parte d
                    if aux_edge['destiny'] == edge['destiny'] or aux_edge['origin'] == edge['origin'] or aux_edge['destiny'] == edge['origin'] or aux_edge['origin'] == edge['destiny']:
                        tree.add(edge['destiny'])
                        tree.add(edge['origin'])
                        cost += edge['weight']
                        break
                    

        
        if len(tree) == nodes + 1:
            break

    return cost

graph, nodes, edges = read_graph()
print(kruskal(graph, nodes, edges ))