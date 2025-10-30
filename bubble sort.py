import time
import random

# Algoritmo Bubble Sort sin bibliotecas adicionales
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        # Se puede optimizar verificando si hubo intercambio
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break

# Función para medir el tiempo de ejecución
def medir_tiempo(lista):
    inicio = time.time()
    bubble_sort(lista)
    fin = time.time()
    return fin - inicio

# Pruebas
tamanos = [1000, 10000, 100000]  

for n in tamanos:
    # Lista aleatoria
    lista_aleatoria = [random.randint(0, n) for _ in range(n)]
    tiempo_aleatorio = medir_tiempo(lista_aleatoria.copy())
    print(f"Bubble Sort con {n} elementos aleatorios: {tiempo_aleatorio:.4f} segundos")

# Lista ya ordenada (10,000)
lista_ordenada = list(range(10000))
tiempo_ordenada = medir_tiempo(lista_ordenada.copy())
print(f"Bubble Sort con 10,000 elementos ordenados: {tiempo_ordenada:.4f} segundos")

# Lista inversa (10,000)
lista_inversa = list(range(10000, 0, -1))
tiempo_inversa = medir_tiempo(lista_inversa.copy())
print(f"Bubble Sort con 10,000 elementos en orden inverso: {tiempo_inversa:.4f} segundos")
