import time

# =============================
# SHELL SORT
# =============================
seed = 123456
def pseudo_rand():
    global seed
    seed = (1103515245 * seed + 12345) & 0x7fffffff
    return seed

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

def medir_tiempo_shell(arr):
    inicio = time.time()
    shell_sort(arr)
    fin = time.time()
    return fin - inicio

# =============================
# PRUEBAS
# =============================
if __name__ == "__main__":
    print("===== SHELL SORT =====")
    tamanos = [1000, 10000, 100000]

    for n in tamanos:
        arr = genera_aleatoria(n)
        print(f"Aleatoria {n:6d}: {medir_tiempo_shell(arr.copy()):.6f} s")
        print(f"Ordenada  {n:6d}: {medir_tiempo_shell(list(range(n))):.6f} s")
        print(f"Inversa   {n:6d}: {medir_tiempo_shell(list(range(n, 0, -1))):.6f} s")
