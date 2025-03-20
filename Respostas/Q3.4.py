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

    def bfs_caminho(self, inicio, fim):
        visitados = set()
        fila = deque([(inicio, [inicio])])

        while fila:
            no, caminho = fila.popleft()
            if no == fim:
                return caminho
            for vizinho in self.adjacencia.get(no, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))

        return None

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
grafo = Grafo(orientado=False)
for origem, destino in arestas:
    grafo.adicionar_aresta(origem, destino)

print(grafo.bfs_caminho("A", "E"))
