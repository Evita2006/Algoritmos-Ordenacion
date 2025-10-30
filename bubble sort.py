import time
import random

# =============================
# BUBBLE SORT
# =============================
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break

def medir_tiempo_bubble(lista):
    inicio = time.time()
    bubble_sort(lista)
    fin = time.time()
    return fin - inicio

# =============================
# PRUEBAS
# =============================
if __name__ == "__main__":
    print("===== BUBBLE SORT =====")
    tamanos = [1000, 10000, 100000]

    for n in tamanos:
        lista_aleatoria = [random.randint(0, n) for _ in range(n)]
        print(f"Aleatoria {n:6d}: {medir_tiempo_bubble(lista_aleatoria.copy()):.4f} s")
        print(f"Ordenada  {n:6d}: {medir_tiempo_bubble(list(range(n))):.4f} s")
        print(f"Inversa   {n:6d}: {medir_tiempo_bubble(list(range(n, 0, -1))):.4f} s")
