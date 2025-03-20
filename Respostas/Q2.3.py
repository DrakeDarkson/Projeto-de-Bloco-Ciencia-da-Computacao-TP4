class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra):
        nodo = self.raiz
        for char in palavra:
            if char not in nodo.filhos:
                nodo.filhos[char] = TrieNode()
            nodo = nodo.filhos[char]
        nodo.fim_palavra = True

    def buscar_nodo(self, prefixo):
        nodo = self.raiz
        for char in prefixo:
            if char not in nodo.filhos:
                return None
            nodo = nodo.filhos[char]
        return nodo

    def obter_palavras(self, nodo, prefixo, resultados):
        if nodo.fim_palavra:
            resultados.append(prefixo)
        for char, prox_nodo in nodo.filhos.items():
            self.obter_palavras(prox_nodo, prefixo + char, resultados)

    def autocomplete(self, prefixo):
        nodo = self.buscar_nodo(prefixo)
        resultados = []
        if nodo:
            self.obter_palavras(nodo, prefixo, resultados)
        return resultados

trie = Trie()
palavras = ["carro", "casa", "gato", "galinha", "caminhão"]
for palavra in palavras:
    trie.inserir(palavra)

print(trie.autocomplete("ca"))
print(trie.autocomplete("ga"))
print(trie.autocomplete("x"))
