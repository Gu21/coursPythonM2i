#Ajouter une tache
def ajout_tache(todo_list):
    taches = (input("Rentrez une tache"))
    todo_list[len(todo_list)+1] = taches
    print(f"La tache {taches} à été ajoutée")


#Affichage de la todolist
def affichage_tache(todo_list):
        for numero_tache, tache in todo_list.items():
            print(f"Liste des tâches de la todo liste: {numero_tache}:{tache}\n")
            
#enlever la tache dans la todo liste
def supprimer_tache(todo_list):
    numero_tache = int((input("Quelle tache enlever ?")))
    if numero_tache in todo_list:
        taches = todo_list.pop(numero_tache)
        print(f"La tache {taches} a été supprimée")


#Todolist avec un dictionnaire initialisé
todo_list = {}


print("========================================")
print("            TODOLIST                    ")
print("========================================")

print("1 - Ajouter une tache")
print("2 -Supprimer une tache")
print("3 - Affichage de la todo list")
print("4 - Quitter")


# Votre programme boucle tant que vous n'avez demandé de sortir.
while True:
    choix = int(input("Saisir votre choix"))
    if choix == 1:
        ajout_tache(todo_list)
    elif choix == 2:
        supprimer_tache(todo_list)
    elif choix == 3:
        affichage_tache(todo_list)
    else:
        print("4 - Quitter")
        print("A bientôt")
        break


