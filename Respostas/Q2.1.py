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

    def exibir(self, nodo=None, prefixo=""):
        if nodo is None:
            nodo = self.raiz
        if nodo.fim_palavra:
            print(prefixo)
        for char, prox_nodo in nodo.filhos.items():
            self.exibir(prox_nodo, prefixo + char)

trie = Trie()
palavras = ["carro", "casa", "gato", "galinha"]
for palavra in palavras:
    trie.inserir(palavra)

trie.exibir()
