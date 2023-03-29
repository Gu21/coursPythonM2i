'''
CREER un programme qui rentre un nombre d'élève un nombre de matière pour chaque eleve et chaque matiere :
demander à l'utilisateur de rentrer des notes (un nombre aléatoire)une fois terminé :
vous faites par élève :
Moyenne dans la matiere
Note la plus haute dans la matiere
Notre la plus basse dans la matiere


Moyenne général
Global :


Moyenne générale de la classeNote la plus haute (élèves et matieres)
Note la plus basse (élèves et matieres)
'''

import random
import statistics



def saisie(nombre_eleve, nombre_matiere):
    for i in range(nombre_eleve):
        eleve = input("Saisir un nom : ")
        matieres = []
        for j in range(nombre_matiere):
            matiere = input("Saisir une matière : ")
            notes = []
            for k in range(random.randint(2,3)):
                note = int(input("Saisir une note : "))
                notes.append(note)
            matieres.append([matiere, notes])
        eleves.append([eleve, matieres])



def moyenne():
    for eleve in eleves:
        for matiere in eleve[1]:
            moyenne = statistics.mean(matiere[1])
            noteHaute = max(matiere[1])
            noteBasse = min(matiere[1])
            print("La moyenne de ",eleve[0]," en ",matiere[0] , " est ", moyenne)
            print("La note la plus haute est : ", noteHaute)
            print("La note la plus basse est : ", noteBasse)
            print("La moyenne de ",eleve[0]," en ", matiere[0] , " est ", moyenne)
            print("La moyenne de ", eleve[0],  " est de: ", moyenne_generale_eleve)
            print("--------------------------------------")





eleves = []
matieres = []
nombre_note = 0
mayenne = 0
nombre_eleve = int(input("Saisir un nombre d'élèves : "))
nombre_matiere = int(input("Saisir un nombre de matières : "))


saisie(nombre_eleve, nombre_matiere)
print(eleves)
moyenne_generale_eleve = sum(moyenne) / nombre_matiere
mayenne = moyenne(nombre_matiere)





