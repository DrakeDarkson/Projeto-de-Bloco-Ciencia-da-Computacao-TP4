import heapq

def inserir_na_heap(heap, elemento):
    heapq.heappush(heap, elemento)

numeros = [10, 5, 20, 1, 8, 15]
heapq.heapify(numeros)

print("Antes da inserção:", numeros)
inserir_na_heap(numeros, 3)
print("Depois da inserção:", numeros)
