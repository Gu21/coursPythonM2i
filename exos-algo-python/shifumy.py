#Jeu : shifumi
#Le jeu propose à deux joueurs de s'affronter sur un duel Shifumi
#le premier arriver à trois à gagner la partie
#cependant la partie continue tant qu'il n'y a pas 2 points d'écarts

#Vous allez le rendre plus modulaire
#separation du moteur et de l'affichage

#vous proposez un menu :
#1) Affrontez un joueur
#2) Affrontez IA
#3) Quittez

#a chaque fin de partie il vous affiche le menu tant que vous n'avez pas quitté.
#Implémentez la partie IIIIAAAA (module random)

'''
from random import randrange

proposition = 'Choisissez shi, fu ou mi: '
shifumi = ['shi', 'fu', 'mi']

def gagnant_manche(saisie1, saisie2):
    if saisie1 == shifumi[0]:
        if saisie2 == shifumi[1]:
            return 2
        elif saisie2 == shifumi[2]:
            return 1
    elif saisie1 == shifumi[1]:
        if saisie2 == shifumi[2]:
            return 2
        elif saisie2 == shifumi[0]:
            return 1
    else:
        if saisie2 == shifumi[0]:
            return 2
        elif saisie2 == shifumi[1]:
            return 1
    return 0

def afficher_gagnant(score):
    if score[0] > score[1]:
        print('Le joueur 1 a gagné')
    else:
        print('Le joueur 2 a gagné')

def afficher_menu():
    choix = int(input('1) Affronter un joueur\n'
                      '2) Affronter IA\n'
                      '3) Quitter\n'
                      'Votre choix: '))
    return choix

def jouer_coup(joueur, choix):
    if choix == 1:
        saisie = ''
        while saisie not in shifumi:
            saisie = input('Joueur ' + str(joueur) + ' - ' + proposition)
        return saisie
    else:
        x = randrange(0,3)
        saisie = shifumi[x]
        print(f"Joueur {joueur} (IA) - joue: {saisie}")
        return saisie

def jouer_manche(choix):
    saisie1 = jouer_coup(1, 1)
    saisie2 = jouer_coup(2, choix)
    return gagnant_manche(saisie1, saisie2)

def update_score(gagnant, score):
    if gagnant == 1:
        score[0] += 1
    elif gagnant == 2:
        score[1] += 1
    print('score1:', score[0], '\tscore2:', score[1], '\n')
    return score

def jouer_partie(choix):
    score = [0,0]
    while abs(score[0] - score[1]) < 2 or (score[0] < 3 and score[1] < 3):
        gagnant = jouer_manche(choix)
        score = update_score(gagnant, score)
    afficher_gagnant(score)

choix = afficher_menu()
while choix != 3:
    jouer_partie(choix)
    choix = afficher_menu()
'''

