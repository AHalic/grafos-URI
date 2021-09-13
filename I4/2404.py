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

# Procura quem é a raiz absoluta de i
def find(parents, i):
    while True:
        # Se o valor é -1 então a raiz é o próprio valor (indice)
        if parents[i] == -1:
            return i
        else:
            i = parents[i]

# Faz a união de dois nós (a raiz do nó destino vira o nó origem)
def union(parents, origin, destiny):
    origin = find(parents, origin)
    destiny = find(parents, destiny)
    parents[origin] = destiny

    return parents

# Le a entrada e preenche o grafo
def read_graph():
    nodes, edges = map(int, input().split())

    # Cria grafo vazio
    graph = []
    for _ in range(edges):
        origin, destiny, weight = map(int, input().split())
        graph.append({
            'origin': origin-1, 
            'destiny': destiny-1,
            'weight': weight,
        })
        # os valores são guardados no grafo com -1 para facilitar o acesso aos indices

    return graph, nodes, edges

def kruskal(graph, nodes, edges):
    # Ordena o grafo com baso nos pesos das arestas
    sorted_graph = sorted(graph, key = lambda k: k['weight'])
    tree_size = 0
    # tree = []
    cost = 0
    
    # Inicializando a estrutura union find
    parents = [-1 for _ in range(nodes)]

    i = 0
    # A mst só terá nodes-1 arestas 
    while tree_size + 1 < nodes:
        edge = sorted_graph[i]

        # Acha as raízes absolutas dos vértices
        parent_origin = find(parents, edge['origin'])
        parent_destiny = find(parents, edge['destiny'])

        # Se forem iguais então a aresta tornaria o grafo ciclico
        if parent_origin == parent_destiny:
            i += 1
            continue
        else:
            # Faz a união e adiciona a conta a aresta na mst (optamos nao salvar)
            parents = union(parents, parent_origin, parent_destiny)
            tree_size += 1
            # tree.append(edge)
            cost += edge['weight']

    return cost

#-------------------------------------------------------------------------------------
graph, nodes, edges = read_graph()
print(kruskal(graph, nodes, edges ))