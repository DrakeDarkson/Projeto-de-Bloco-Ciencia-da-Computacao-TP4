import heapq

def criar_heap(lista):
    heapq.heapify(lista)
    return lista

def exibir_heap(heap):
    print(heap)

numeros = [10, 5, 20, 1, 8, 15]
heap = criar_heap(numeros)
exibir_heap(heap)
