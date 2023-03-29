def deplacer_palet(palets, deplacement_tour1, deplacement_tour2, deplacement_tour3):
    if palets == 0:
        return 1
    elif palets > 0:
        deplacer_palet(palets - 1, deplacement_tour1, deplacement_tour2, deplacement_tour3)
        print(f"Déplacement de la {deplacement_tour1} vers la tour {deplacement_tour3}")
        deplacer_palet(palets - 1, deplacement_tour2, deplacement_tour2, deplacement_tour3)
        print(f"Déplacement de la {deplacement_tour2} vers la tour {deplacement_tour3}")
           

      
tour1 = "tour: 1"
tour2 = "tour: 2"
tour3 = "tour: 3"
nbre_palets = 0
   
nbre_palets = int(input("Veuillez rentrer un nombre de disque:"))
deplacer_palet( nbre_palets, tour1, tour2, tour3)