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
    graph = [[sys.maxsize for i in range(nodes)] for _ in range(nodes)]

    for _ in range(edges):
        origin, destiny, weight = map(int, input().split())
        
        graph[origin - 1][destiny - 1] = weight
        graph[destiny - 1][origin - 1] = weight
        
    return graph, nodes


def PrimTeste(adjacencyMatrix, vertices):
    cost = 0
    # Defining a really big number:
    positiveInf = float('inf')

    selectedVertices = [False for vertex in range(vertices)]

    mstMatrix = [[0 for column in range(vertices)] for row in range(vertices)]

    # While there are vertices that are not included in the MST, keep looking:
    while False in selectedVertices:

        # We use the big number we created before as the possible minimum weight
        minimum = positiveInf

        # The starting vertex
        start = 0

        # The ending vertex
        end = 0

        for i in range(0,vertices):
            # If the vertex is part of the MST, look its relationships
            if selectedVertices[i]:
                # Again, we use the Symmetric Matrix as an advantage:
                for j in range(0+i,vertices):
                    # If the vertex analyzed have a path to the ending vertex AND its not included in the MST to avoid cycles)
                    if (not selectedVertices[j] and adjacencyMatrix[i][j]>0):  
                        # If the weight path analyzed is less than the minimum of the MST
                        if adjacencyMatrix[i][j] < minimum:
                            # Defines the new minimum weight, the starting vertex and the ending vertex
                            minimum = adjacencyMatrix[i][j]
                            start, end = i, j
        
        # Since we added the ending vertex to the MST, it's already selected:
        selectedVertices[end] = True

        # Filling the MST Adjacency Matrix fields:
        mstMatrix[start][end] = minimum
        # Initially, the minimum will be Inf if the first vertex is not connected with itself, but really it must be 0:
        if minimum == positiveInf:
            mstMatrix[start][end] = 0
        else:
            cost += minimum
            
        # Symmetric matrix, remember
        mstMatrix[end][start] = mstMatrix[start][end]

    # Show off:
    print(mstMatrix)
    cost -= minimum
    print(cost)





def prim(graph, graph_size):
    graph_nodes = {i for i in range(graph_size)}
    # graph_visited = set()
    tree = [0 for i in range(graph_size)]
    cost = 0
        
    u = 0
    graph_visited = {u}

    while graph_size > (len(graph_visited)):
        print(f"tam visit {len(graph_visited)} e tamgraph {graph_size}")
        counter = 0
        print(f"Verificando u: {u}", "row:", graph[u])

        while True:
            counter += 1
            u_dist = min(graph[u])
            print("u_dis: ", u_dist)
            w = graph[u].index(u_dist)
            
            if counter == 6:
                print("Quit")
                quit()
                

            if w not in graph_visited or u_dist == sys.maxsize:
                break
            else:
                graph[u][w] = graph[w][u] = sys.maxsize
        
        print(f"Primeiro w: {w}")

        aux_u = u
        aux_w = w
        min_dist = u_dist
        for node in graph_visited - {u}:
            aux_dist = min(graph[node])
            print("Node:", node, graph[node])
    
            if min_dist > aux_dist:
                    min_dist = aux_dist
                    aux_w = graph[node].index(aux_dist)
                    aux_u = node

            # if aux_w not in graph_visited or u_dist == sys.maxsize:
            #     break
            # else:
            #     graph[u][w] = graph[w][u] = sys.maxsize

        graph[aux_u][aux_w] = sys.maxsize
        graph[aux_w][aux_u] = sys.maxsize

        graph_visited.add(aux_w)
        print(f"ligando: {aux_w} para {aux_u}. tam visit: {graph_visited}")
        cost += min_dist
        print("cost:", cost)
        u = aux_w
        print()
    
    return cost
        

graph, nodes = read_graph()

# print(prim(graph, nodes))

PrimTeste(graph, nodes)

''''

'''