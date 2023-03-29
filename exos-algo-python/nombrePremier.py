#donner un nombre et determiner tous les nombres premiers précédents.
def liste_premier(n, k = 2, liste = []):
    if k > n:
        return liste
    for premier in liste:
        if k % premier == 0:
            return liste_premier(n, k+1, liste)
    liste.append(k)
    return liste_premier(n, k+1, liste)

n = int(input('Veuillez entrer un nombre :'))
print(f'Voici la liste de tous les premiers inférieurs à {n} : {liste_premier(n)}')
