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


# def read_graph():
#     nodes, edges = map(int, input().split())

#     # Cria grafo vazio
#     graph = [{"connections": [], "weights": []} for _ in range(nodes)]

#     for _ in range(edges):
#         origin, destiny, weight = map(int, input().split())
        
#         graph[origin - 1]['connections'].append(destiny - 1)
#         graph[destiny - 1]['connections'].append(origin - 1)
        
#         graph[origin - 1]['weights'].append(weight)
#         graph[destiny - 1]['weights'].append(weight)

#     return graph, nodes, edges

def read_graph():
    nodes, edges = map(int, input().split())

    # Cria grafo vazio
    graph = [[sys.maxsize for i in range(nodes)] for _ in range(nodes)]

    for _ in range(edges):
        origin, destiny, weight = map(int, input().split())
        
        graph[origin - 1][destiny - 1] = weight
        graph[destiny - 1][origin - 1] = weight
        
    return graph, nodes

def prim(graph, graph_size):
    graph_nodes = {i for i in range(graph_size)}
    # graph_visited = set()
    tree = [0 for i in range(graph_size)]
    cost = 0
    

    # [inf,inf,3,4,inf]
    # [inf,inf,5,7,3]
    # [3,5,inf,1,inf]
    # [4,7,1,inf,inf]
    # [inf,3,inf,inf,inf]
    #   0
    # /  \
    # 2 - 3
    # \  /
    #  1 - 4

    # {0,,}
    # u = 0
    # u_dist = 3
    # w = 2
    # w_dist = 0
    
    u = 0
    graph_visited = {u}
    print(*graph, sep="\n")

    while graph_size - (len(graph_visited)):
        counter = 0
        print(f"Verificando u: {u}")
        while True:
            counter += 1
            if counter == 6:
                print("quit")
                quit()
                
            u_dist = min(graph[u])
            w = graph[u].index(u_dist)
            if w not in graph_visited or u_dist == sys.maxsize:
                # graph[u][w] = sys.maxsize
                break
        print(f"Primeiro w: {w}")
        aux = w
        min_dist = u_dist
        for node in graph_visited - {u}:
            aux_dist = min(graph[node])

            if min_dist > aux_dist:
                min_dist = aux_dist
                aux = node
        print(*graph, sep="\n")

        graph[u][aux] = sys.maxsize
        graph[aux][u] = sys.maxsize

        graph_visited.add(aux)
        print(f"ligando: {aux} para {u}. tam visit: {graph_visited}")
        cost += min_dist
        u = aux
    
    return cost
        

graph, nodes = read_graph()

print(prim(graph, nodes))


''''

'''