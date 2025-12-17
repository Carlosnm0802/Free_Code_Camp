import time


def sum(numbers):
    """
    Funcion que haga una suma de numeros desde 1 hasta n
    Complejidad O(n)
    Recorres todos los numeros hasta n para hacer la suma
    Implica n operaciones
    El tiempo crece proporcionalmente a n
    """
    total = 0
    for numbers in range(1,numbers+1):
        total+=numbers
    return total

def formula(n):
    """
    Funcion que haga la formula matematica de la suma
    Complejidad O(1)
    No importa el valor de n, siempre se hacen las mismas operaciones
    El tiempo es constante y no crece con n
    """
    return n*(n+1)//2

inicio = time.time()
resultado=sum(1000000)
fin = time.time()
print("Resultado suma:", resultado)
print("Tiempo suma O(n):", fin - inicio)

inicio = time.time()
resultado=formula(1000000)
fin = time.time()
print("Resultado suma:", resultado)
print("Tiempo suma O(1):", fin - inicio)