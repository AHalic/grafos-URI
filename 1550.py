# Funcao para inverter o numero
def inversao(num):
    aux = 0
    while (num > 0):    
        remainder = num % 10  
        aux = (aux * 10) + remainder  
        num = num // 10  

    return aux
    
def busca(inicial, resultado):
    # Adiciona vertice a lista de busca e colecao de vertices percorridas
    busca = [(inicial, 0)]
    historico = {inicial}
        
    while True:
        vertice_buscado, altura = busca.pop(0)
        altura += 1

        soma, invertido = vertice_buscado + 1, inversao(vertice_buscado)
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