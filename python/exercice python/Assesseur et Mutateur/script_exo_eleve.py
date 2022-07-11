

# creer fonction qui classe eleve dans sectiopn selon age 
# Demander si secretaire ou professeur 
    # si secretaire proposer :
        # - ajouter eleve
        # - declarer anniversaire
    
    # ajouter eleve stocker dans un tableau
    
    # si professeur proposer : 
        # quel eleve il veut changer de section
        # dans quel section il veut mettre l'eleve 
while True :
    utilisateur = int(input('Entrez 1 : pour secretaire.\nEntrez 2 : pour professeur.\n'))

    if utilisateur == 1 :
        
        choix = int(input('Voulez-vous:\n\t1.Ajouter un élève ? :  Entrez 1\n\t2.Declarer un anniversaire ? : Entrez 2\n'))
        
        if choix == 1 :
            print('fonction ajoutez eleve')
        elif choix ==2 :
            print('fonction declarer anniversaire')
        
            
    elif utilisateur == 2 :
       eleve = input('Quel élève voulez vous changer de section ?')     
        # donnez choix de trouver par son nom puis prenom puis demandez dans quel section le metre.
        
           