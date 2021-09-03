# -*- coding: utf-8 -*-

#--------------------------FUNCOES--------------------------
def inversao(num):
    """
        Funcao para inverter o numero
        `param` num: numero para ser invertido
    """
    aux = 0
    while (num > 0):    
        remainder = num % 10  
        aux = (aux * 10) + remainder  
        num = num // 10  

    return aux
    
def busca(inicial, resultado):
    """
        Dado um valor inicial e um final (resultado), cria um grafo e percorre ele em largura
        durante o preenchimento.
        `param` inicial: valor da vertice inicial
        `param` resultado: valor do vertice destino       
    """

    # Adiciona vertice a lista de busca e conjunto de vertices percorridas
    busca = [(inicial, 0)]
    historico = {inicial}
        
    while True:
        # Pega a primeira vertice da fila 
        vertice_buscado, altura = busca.pop(0)
        altura += 1

        # Possibilidade dos boteoes de soma e inversao
        soma, invertido = vertice_buscado + 1, inversao(vertice_buscado)

        if soma == resultado or invertido == resultado:
            return altura
        
        # Se o vertice soma nao esta no conjunto de vertices percorridos, ele eh adicionado
        # ao conjunto e fila
        if soma not in historico:
            busca.append((soma, altura))
            historico.add(soma)
        
        # Se o vertice invertido nao esta no conjunto de vertices percorridos, ele eh adicionado
        # ao conjunto e fila
        if invertido not in historico:
            busca.append((invertido, altura))
            historico.add(invertido)

#--------------------------MAIN--------------------------

# Leitura
num_casos = int(input())

while num_casos:
    # Ler inicio (A) e final (B)
    inicio, resultado = list(map(int,input().split()))

    # Busca de largura para encontrar menor quantidade de apertos de botoes e depois apresenta
    min_apertos = busca(inicio, resultado)
    print(min_apertos)
    
    # Atualizacao de quantos casos faltam 
    num_casos -= 1