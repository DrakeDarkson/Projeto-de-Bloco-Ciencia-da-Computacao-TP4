import heapq

def remover_raiz(heap):
    if heap:
        heapq.heappop(heap)

numeros = [5, 2, 3, 7, 1]
heapq.heapify(numeros)

print("Antes da remoção:", numeros)
remover_raiz(numeros)
print("Depois da remoção:", numeros)
