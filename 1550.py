def adiciona(num):
    return num + 1

def inversao(num):
    tam = len(str(num))
    aux = str(num)[::-1]
    
    while len(aux) < tam:
        aux += "0"

    return int(aux)

def gera_nivel(valores_anteriores):
    valores_novos = []
    for i in valores_anteriores:
        invertido = inversao(i)
        soma = adiciona(i)
        if not (soma in valores_anteriores):
            valores_novos.append(soma)
        
        if not (inversao in valores_anteriores):
            valores_novos.append(invertido)

    return valores_novos

# Leitura
num_casos = int(input())

conjuntos = []
for i in range(num_casos):
    original, final = input().split()
    conjuntos.append((original, final))

# Algoritmo
for i, par in enumerate(conjuntos):
    inicio, resultado = int(par[0]), int(par[1])
    
    print(inicio, resultado)

    cont = 0
    resolvido = False

    if inicio == resultado:
        print(0)
        continue

    soma, mult = inicio, inicio

    while not resolvido:
        soma, inver = adiciona(soma), adiciona(mult) 

    print(cont)
