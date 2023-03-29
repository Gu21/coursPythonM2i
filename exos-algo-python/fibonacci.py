#ecrire la suite de Fibonacci en récursif fib(n)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Veuillez saisir la valeur de n : "))
print(f"Le terme de rang {n} de la suite de Fibonacci vaut {fibonacci(n)}.")
