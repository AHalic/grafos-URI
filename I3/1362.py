import sys 

# Dicionario usado pra encontrar o valor no grafo
tamanhos_indice = {
    'XS': 1,
    'S': 2,
    'M': 3,
    'L': 4,
    'XL': 5,
    'XXL': 6
}

# Procura o vertice de menor peso na arvore
def find_min(pesos, arvore, tam):
    aux_min = sys.maxsize
    node = tam - 1

    # Busca no vetor
    for i in range(tam):
        # Procura vertice que ainda não esteja na arvore e tenha menor peso
        if pesos[i] < aux_min and i not in arvore:
            aux_min = pesos[i]
            node = i
    return node
    
def dijkstra(grafo, tam):
    # Inicializa o vetor de pesos com um valor muito grande
    pesos = [sys.maxsize] * tam
    
    # Escolhe o ponto inicial e modifica o peso
    pesos[0] = 0
    visitados = set()
    sumidouro = tam - 1

    # Vetor de pais usado para saber qual corte achado (pra ser usado no Ford)
    pais = [i for i in range(tam)]

    while sumidouro not in visitados:
        # Acha o vertice de menor peso e adiciona ele
        u = find_min(pesos, visitados, tam)
        visitados.add(u)
        
        # Relaxa os vertices vizinhos de u
        for w in range(tam):
            dist_w = pesos[u] + grafo[u][w]
            if grafo[u][w] != 0 and w not in visitados and pesos[w] > dist_w:
                pesos[w] = dist_w
                pais[w] = u

    # Retorna a arvore encontrada
    return pais

def ford_fulkerson(grafo, tam):
    fluxo_max = 0
    sumidouro = tam - 1

    # Encontra o corte
    pais = dijkstra(grafo, tam)

    # Enquanto for possível alcançar t
    while pais[sumidouro] != sumidouro:
        # Encontra no que chegou no sumidouro
        aux_origem = pais[sumidouro]
        aux_destino = sumidouro

        while True:
            # Altera o fluxo de ida e volta
            grafo[aux_origem][aux_destino] -= 1
            grafo[aux_destino][aux_origem] += 1
            
            # Encontra a conexao
            aux_destino = aux_origem
            aux_origem = pais[aux_origem]

            # Até encontrar o vértice s (origem)
            if aux_destino == 0:
                break

        # Fluxo do corte (neste grafo) sempre é 1
        fluxo_max += 1
        pais = dijkstra(grafo, tam)

    return fluxo_max

########### Leitura

casos = int(input())

for _ in range(casos):
    camisas, voluntarios = map(int, input().split())
    
    # Qtd de vertices do grafo: 6 tamanhos de blusa + n voluntarios + origem e sumidouro
    nos = 6 + voluntarios + 2

    # Cria grafo
    grafo = [[0 for i in range(6 + voluntarios + 2)] for _ in range(6 + voluntarios + 2)]
    
    qtd_camisas = int(camisas/6)

    # Cria conexoes do grafo de blusas para sumidouro
    for i in range(1, 7):
        grafo[voluntarios+i][len(grafo)-1] = qtd_camisas

    # Cria conexoes grafos de voluntarios para blusas
    for i in range(1, voluntarios+1):
        tamanho1, tamanho2 = map(str, input().split())

        # conexoes origem - voluntarios
        grafo[0][i] = 1

        # conexoes voluntarios - blusas
        grafo[i][voluntarios+tamanhos_indice[tamanho1]] = 1
        grafo[i][voluntarios+tamanhos_indice[tamanho2]] = 1
    
    # Apresenta resposta
    if ford_fulkerson(grafo, nos) == voluntarios:
        print("YES")
    else:
        print("NO")
