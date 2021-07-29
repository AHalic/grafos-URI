# -*- coding: utf-8 -*-
valor_A = ord("a")

########################################################
# Classe referente ao grafo

class Grafo:
    """
        Classe destinada para armazenar lista de adjacencia.
    """

    def __init__(self, vertices=0, arestas=0):
        """
            Construtor de Lista. Inicializa uma lista vazia do 
            tamanho do numero de vertices

            `param` vertices: numero de vertices 
            `param` arestas: numero de arestas
        """

        self.num_vertices = vertices
        self.num_arestas = arestas

        self.vertices = []
        

        # Inicializa lista do tamanho de verticies com cada
        # inidice uma lista vazia
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
        self.vertices[index]["visitado"] = True

    def visitado(self, index):
        return self.vertices[index]["visitado"]

    def __len__(self):
        return len(self.vertices)
    
    def len_destino(self, index):
        return len(self.vertices[index]["destino"])

    def destino(self, index):
        return self.vertices[index]["destino"]

    # def __str__(self):
    #     resposta = ""
    #     # Anda pelos vertices
    #     for i, conjuntos in enumerate(self.vertices):
    #         resposta += json.dump(conjuntos, indent=4)

    #     return resposta

def pathR(grafo, index, comp):
    # Verifica primeiro se o vertice daquele indice foi visitado
    if not grafo.visitado(index):
        # Adiciona letra para lista da componente conexa
        comp.append(chr(valor_A + index))
        grafo.set_visitado(index)
        # print(f"Visitando {index} com conexões a {grafo.destino(index)}")
        for i in grafo.destino(index):
            comp = pathR(grafo, i, comp)
            # print(f"Visitando: {i} e list {comp}")
        
        # print()
    return comp


########################################################

if __name__ == "__main__":
    aux = ord("a")
    
    # Leitura da entrada e insercao dos vertices nos grafos
    testes = int(input())
    for i in range(testes):
        num_vertice, num_arestas = input().split()
        num_vertice, num_arestas = int(num_vertice), int(num_arestas)
        grafo = Grafo(num_vertice, num_arestas)
        
        for _ in range(num_arestas):
            origem, destino = input().lower().split()
            id_origem, id_destino = ord(origem) - aux, ord(destino) - aux
            grafo.adiciona_aresta(id_origem, id_destino)
          
        print(f"Case #{i+1}:")
        cont = 0
        for i in range(num_vertice):
            comp = []
            comp = pathR(grafo, i, comp)
            if len(comp):
                cont += 1
                comp.sort()
                print(*comp, "", sep=",")    
        print(f"{cont} connected components", end="\n\n")    
    
    