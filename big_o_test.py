def sum(numbers):
    """
    Funcion que haga una suma de numeros desde 1 hasta n
    Complejidad O(n)
    """
    total = 0
    for numbers in range(1,numbers+1):
        total+=numbers
    return total

def formula(n):
    """
    Funcion que haga la formula matematica de la suma
    Complejidad O(1)
    """
    return n*(n+1)//2