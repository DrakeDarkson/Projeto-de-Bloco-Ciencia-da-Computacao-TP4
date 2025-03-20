from collections import deque

class Grafo:
    def __init__(self, orientado=False):
        self.adjacencia = {}
        self.orientado = orientado

    def adicionar_aresta(self, origem, destino):
        if origem not in self.adjacencia:
            self.adjacencia[origem] = []
        self.adjacencia[origem].append(destino)
        if not self.orientado:
            if destino not in self.adjacencia:
                self.adjacencia[destino] = []
            self.adjacencia[destino].append(origem)

    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        resultado = []

        visitados.add(inicio)

        while fila:
            no = fila.popleft()
            resultado.append(no)
            for vizinho in self.adjacencia.get(no, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        return resultado

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
grafo = Grafo(orientado=False)
for origem, destino in arestas:
    grafo.adicionar_aresta(origem, destino)

print(grafo.bfs("A"))
