#la factorielle

def factorielle(n):
    if n <= 1:
        return 1
    else:
        return n*factorielle(n-1)
    
n = int(input('Veuillez entrer un nombre : '))
print(f'{n}! = {factorielle(n)}')


#En ternaire
# return 1 if n < 2 else n*factorielle(n-1)