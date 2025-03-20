import heapq

def buscar_na_heap(heap, elemento):
    return elemento in heap

numeros = [10, 5, 20, 1, 8, 15]
heapq.heapify(numeros)

print(buscar_na_heap(numeros, 8))
print(buscar_na_heap(numeros, 12))
