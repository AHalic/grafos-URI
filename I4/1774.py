'''
Algoritmo de Prim

1. T ← vazio;
2. V' ← {u};
3. para-todo v E V – V'  faça
4.      L(v) ← peso ({u,v});
5. fim-para-todo
6. enquanto V' !=  V faça
7.      ache um vértice w tal que L(w) = min {L(v) | v E V-V'};
8.      u = o vértice de V', ligado a w, representando a aresta com o menor custo;
9.      e = {u,w};
10.     T ← T U {e};
11.     V'← V' U {w};
12.     para-todo v E V – V' faça
13.         se peso({v,w}) < L(v) então
14.             L(v) ← p({v,w});
15.         fim-se
16.     fim-para-todo
17. fim-enquanto
'''
import sys

def read_graph():
    nodes, edges = map(int, input().split())

    # Cria grafo vazio
    graph = [[0 for i in range(nodes)] for _ in range(nodes)]

    for _ in range(edges):
        origin, destiny, weight = map(int, input().split())
        # preenche o grafo com os nós -1 para facilitar com indices
        graph[origin - 1][destiny - 1] = weight
        graph[destiny - 1][origin - 1] = weight
        
    return graph, nodes


# Procura o vertice de menor peso na arvore
def findMin(weights, tree):
    min = sys.maxsize
    node = -1

    # Busca no vetor
    for i in range(len(weights)):
        # Procura vertice que ainda não esteja na arvore e tenha menor peso
        if weights[i] < min and i not in tree:
            min = weights[i]
            node = i
    return node
    
        

def prim(graph, nodes):
    # Inicializa o vetor de pesos com um valor muito grande
    weights = [sys.maxsize for i in range(nodes)]
    # Escolhe o ponto inicial e modifica o peso
    weights[0] = 0
    tree = set()

    while len(tree) + 1 < nodes:
        # acha o vertice de menor peso e adiciona ele a mst
        u = findMin(weights, tree)
        tree.add(u)

        # relaxa os vertices
        for w in range(nodes):
            # o peso será modificado se o nó n estiver na mst
            # e se for menor do que o peso já achado
            if graph[u][w] != 0 and w not in tree and graph[u][w] < weights[w]:
                weights[w] = graph[u][w]

    # retorna a soma dos pesos (equivalente ao custo total)
    return sum(weights)


        

graph, nodes = read_graph()

print(prim(graph, nodes))
