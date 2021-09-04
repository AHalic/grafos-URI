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
    graph = [{"connections": [], "weights": []} for _ in range(nodes)]

    for _ in range(edges):
        origin, destiny, weight = map(int, input().split())
        
        graph[origin - 1]['connections'].append(destiny - 1)
        graph[destiny - 1]['connections'].append(origin - 1)
        
        graph[origin - 1]['weights'].append(weight)
        graph[destiny - 1]['weights'].append(weight)

    return graph, nodes, edges

def read_graph():
    nodes, edges = map(int, input().split())

    # Cria grafo vazio
    graph = [[sys.maxsize for i in range(nodes)] for _ in range(nodes)]

    for _ in range(edges):
        origin, destiny, weight = map(int, input().split())
        
        graph[origin - 1][destiny - 1] = weight
        graph[destiny - 1][origin - 1] = weight
        
    return graph, nodes, edges

def prim(graph, graph_size):
    tree = [[] for _ in range(graph_size)]
    
    graph_set = {i for i in range(graph_size)}
    visited = {0}

    dist = [sys.maxsize for _ in range(graph_size)]

    for i in graph[0]['connections']:
        node = graph[0]['connections'][i]
        dist[node] = graph['weights'][i]

    while len(visited) != graph_size:
        l_w = min(dist)
        w = dist.index(l_w)

        u = min(graph[l_w]['connections'])

        


graph, nodes, edges = read_graph()

print(graph)

''''

'''