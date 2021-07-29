def adiciona(num):
    return num + 1

def inversao(num):
    aux = 0
    while (num > 0):  
        # Logic  
        remainder = num % 10  
        aux = (aux * 10) + remainder  
        num = num // 10  

    return aux

def gera_vertices(valores_anteriores, historico, resultado):
    valores_novos = []
    for i in valores_anteriores:
        soma = adiciona(i)
        invertido = inversao(i)

        if soma == resultado:
            return [resultado]
        elif invertido == resultado:
            return [resultado]

        if soma not in historico and soma not in valores_novos:
            valores_novos.append(soma)
        
        if invertido not in historico and invertido not in valores_novos:
            valores_novos.append(invertido)

    # valores_novos.sort()
    # print(valores_novos)
    return valores_novos

if __name__ == "__main__":
    # Leitura
    num_casos = int(input())

    for i in range(num_casos):
        original, final = input().split()
        inicio, resultado = int(original), int(final)

        cont = 0
        grafo = [inicio]
        vertices = [inicio]

        while resultado not in vertices:
            vertices = gera_vertices(vertices, grafo, resultado)
            grafo += vertices
            cont += 1

        print(cont)

#  513 8932