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

trie = Trie()
palavras = ["carro", "casa", "gato", "galinha"]
for palavra in palavras:
    trie.inserir(palavra)

print(trie.buscar("casa"))
print(trie.buscar("cachorro"))
