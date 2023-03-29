#pour une chaine de caracteres, determine par recursivite sa longueur

#rendre recursif
def longueur(chaine):
    if chaine == '':
        return 0
    else: 
        return 1 + longueur(chaine[1:])

#chaine = input('Veuillez entrer une chaine: ')
#print(f"Votre chaine a pour longueur {longueur(chaine)}")




# Ecrire une fonction récursive « Binaire » permettant d’imprimer à l’écran la représentation binaire d’un nombre N.

def binary(x):    
    if x == 0:
        return '0'
    elif x == 1:
        return '1'
    else:
        return binary(x >> 1) + str(x & 1)

x = int(input('Veuillez saisir un nombre: '))
binary(x)












