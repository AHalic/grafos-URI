tamanhos_indice = {
    'XS': 1,
    'S': 2,
    'M': 3,
    'L': 4,
    'XL': 5,
    'XXL': 6
}



casos = int(input())

for _ in range(casos):
    camisas, voluntarios = map(int, input().split())
    
    graph = [[0 for i in range(6 + voluntarios + 2)] for _ in range(6 + voluntarios + 2)]
    
    for i in range(1, 7):
        graph[voluntarios+i][len(graph)-1] = int(camisas/6)

    for i in range(1, voluntarios+1):
        tamanho1, tamanho2 = map(str, input().split())
        graph[0][i] = 1
        graph[i][voluntarios+tamanhos_indice[tamanho1]] = 1
        graph[i][voluntarios+tamanhos_indice[tamanho2]] = 1
    

"""
[
0           s
1-N         (N voluntarios)
N+1-N+6     6 camisas
len         t
]

"""