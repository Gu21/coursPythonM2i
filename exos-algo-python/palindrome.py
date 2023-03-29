#ecrire un programme qui determine si un mot est un palindrome.
def palindrome(chaine):
    return palindrome_inner(chaine.lower())

def palindrome_inner(chaine):
    if chaine == '':
        return True
    elif chaine[0] == chaine[-1]:
        return palindrome_inner(chaine[1:-1])
    else:
        return False

saisie = input('Veuillez entrer une chaine : ')
if palindrome(saisie):
    print(f"{saisie} est un palindrome")
else:
    print(f"{saisie} n'est pas un palindrome")
