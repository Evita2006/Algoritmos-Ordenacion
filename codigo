#!/usr/bin/env python3

# Generador congruencial simple para no usar random
seed = 123456
def pseudo_rand():
    global seed
    seed = (1103515245 * seed + 12345) & 0x7fffffff
    return seed

# Shell Sort
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def genera_aleatoria(n):
    return [pseudo_rand() % 100000 for _ in range(n)]

def mide(nombre, arr):
    import time
    t0 = time.time()
    shell_sort(arr)
    t1 = time.time()
    print(f"{nombre}: {t1 - t0:.6f} segundos")

def main():
    # Tamaños solicitados
    arr1 = genera_aleatoria(1000)
    arr2 = genera_aleatoria(10000)
    arr3 = genera_aleatoria(100000)

    arr_sorted = list(range(10000))          # ya ordenados
    arr_reverse = list(range(10000, 0, -1))  # inversos

    mide("1000 aleatorios", arr1)
    mide("10000 aleatorios", arr2)
    mide("100000 aleatorios", arr3)
    mide("10000 ordenados", arr_sorted)
    mide("10000 inversos", arr_reverse)

if __name__ == "__main__":
    main()
