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

    def dfs(self, inicio):
        visitados = set()
        resultado = []

        def explorar(no):
            if no not in visitados:
                visitados.add(no)
                resultado.append(no)
                for vizinho in self.adjacencia.get(no, []):
                    explorar(vizinho)

        explorar(inicio)
        return resultado

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
grafo = Grafo(orientado=False)
for origem, destino in arestas:
    grafo.adicionar_aresta(origem, destino)

print(grafo.dfs("A"))
