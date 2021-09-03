# -*- coding: utf-8 -*-


#--------------------------CLASSE GRAFO--------------------------

class Grafo:
    """
        Classe destinada para armazenar lista de adjacencia de representação do grafo
    """

    def __init__(self, vertices=0, arestas=0):
        """
            Construtor de Lista. Inicializa uma lista vazia do 
            tamanho do numero de vertices

            `param` vertices: numero de vertices do grafo
            `param` arestas: numero de arestas do grafo
        """

        self.num_vertices = vertices
        self.num_arestas = arestas

        self.vertices = []
        
        # Preenche lista de vertices, sendo cada vertice composto
        # de uma lista de vertices destino e se este já foi visitado
        for vertice in range(self.num_vertices):
            vertice_formato = {
                "destino": [],
                "visitado": False
            }
            self.vertices.append(vertice_formato)

    def adiciona_aresta(self, origem, destino):
        """
            Adiciona aresta para lista.  

            `param` origem: valor do vertice origem
            `param` destino: valor do vertice destino
        """

        # Cria a aresta de origin->destino e destino->origem
        self.vertices[origem]["destino"].append(destino)
        self.vertices[destino]["destino"].append(origem)


    def set_visitado(self, index):
        """
            Modifica  o status de modificado para True

            `param` index: indice do vertice na lista de vertices
        """
        self.vertices[index]["visitado"] = True

    def visitado(self, index):
        """
            Retorna o status de visitado do vertice

            `param` index: indice do vertice no grafo
        """
        return self.vertices[index]["visitado"]
    
    def len_destino(self, index):
        """
            Retorna a quantidade de vértices ligadas ao vértice desejado

            `param` index: indice do vertice no grafo
        """
        return len(self.vertices[index]["destino"])

    def destino(self, index):
        """
            Retorna a lista de vértices ligados ao vértice desejado

            `param` index: indice do vertice no grafo
        """
        return self.vertices[index]["destino"]



#--------------------------CONSTANTE--------------------------
# Define valor asc referente a letra a
valor_A = ord("a")



#--------------------------FUNCOES--------------------------

def pathR(grafo, index, componente_conexa):
    """
        Realiza a busca em profundidade e acha uma componente conexa

        `param` grafo: grafo em que será feita a busca
        `param` index: indice do vertice no grafo
        `param` componente_conexa: lista vazia que será preenchida com a componente conexa
    """

    # Verifica primeiro se o vertice daquele indice foi visitado
    if not grafo.visitado(index):
        # Adiciona a letra (vertice) para a lista da componente conexa
        componente_conexa.append(chr(valor_A + index))

        grafo.set_visitado(index)

        # Chama recursivamente a função para todos os vértices ligados a este
        for i in grafo.destino(index):
            componente_conexa = pathR(grafo, i, componente_conexa)

        
    return componente_conexa




#--------------------------MAIN--------------------------

if __name__ == "__main__":
    # Leitura da entrada e insercao dos vertices nos grafos
    testes = int(input())
    
    for i in range(testes):
        num_vertice, num_arestas = list(map(int,input().split()))

        grafo = Grafo(num_vertice, num_arestas)
        
        # Le todas as arestas e preenche o grafo
        for _ in range(num_arestas):
            origem, destino = list(map(ord,input().split()))

            id_origem, id_destino = origem - valor_A, destino - valor_A

            grafo.adiciona_aresta(id_origem, id_destino)


        print(f"Case #{i+1}:")
        contador = 0
        
        # Chama a função pathR para cada vértice do grafo
        for i in range(num_vertice):
            componente_conexa = pathR(grafo, i, [])
            
            # Caso a componente conexa não esteja vazia, ordena e imprime a lista
            if len(componente_conexa):
                contador += 1
                componente_conexa.sort()
                print(*componente_conexa, "", sep=",")    

        print(f"{contador} connected components", end="\n\n")    
    
    