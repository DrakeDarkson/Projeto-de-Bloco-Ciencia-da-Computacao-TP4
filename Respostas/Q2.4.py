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

    def buscar(self, palavra):
        nodo = self.raiz
        for char in palavra:
            if char not in nodo.filhos:
                return False
            nodo = nodo.filhos[char]
        return nodo.fim_palavra

    def remover(self, palavra):
        def _remover(nodo, palavra, profundidade):
            if profundidade == len(palavra):
                if not nodo.fim_palavra:
                    return False
                nodo.fim_palavra = False
                return len(nodo.filhos) == 0
            char = palavra[profundidade]
            if char not in nodo.filhos:
                return False
            remover_proximo = _remover(nodo.filhos[char], palavra, profundidade + 1)
            if remover_proximo:
                del nodo.filhos[char]
                return len(nodo.filhos) == 0 and not nodo.fim_palavra
            return False

        _remover(self.raiz, palavra, 0)

trie = Trie()
palavras = ["casa", "casamento", "casulo", "cachorro"]
for palavra in palavras:
    trie.inserir(palavra)

print(trie.buscar("casa"))
trie.remover("casa")
print(trie.buscar("casa"))
print(trie.buscar("casamento"))
print(trie.buscar("casulo"))
