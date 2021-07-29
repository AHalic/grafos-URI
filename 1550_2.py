def inversao(num):
    aux = 0
    while (num > 0):    
        remainder = num % 10  
        aux = (aux * 10) + remainder  
        num = num // 10  

    return aux
    
def busca(inicial, resultado):
    # Adiciona vertice a lista de busca e historico de vertices percorridas
    busca = [(inicial, 0)]
    historico = {inicial}

    fila_cheia = len(busca) > 0
    
    while fila_cheia:
        vertice_buscado, altura = busca.pop(0)
        soma, invertido = vertice_buscado + 1, inversao(vertice_buscado)
        
        altura += 1
        if soma == resultado or invertido == resultado:
            return altura
        
        if soma not in historico:
            busca.append((soma, altura))
            historico.add(soma)
        
        if invertido not in historico:
            busca.append((invertido, altura))
            historico.add(invertido)

# Leitura
num_casos = int(input())

while num_casos:
    # Ler inicio (A) e final (B)
    inicio, resultado = list(map(int,input().split()))

    # Busca de largura para encontrar menor quantidade de apertos de botoes
    min_apertos = busca(inicio, resultado)
    
    num_casos -= 1
    print(min_apertos)