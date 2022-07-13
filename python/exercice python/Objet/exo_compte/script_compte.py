from classe_compte import *
from datetime import date

mon_compte = Compte(date_creation = date.today(), solde = 0, proprio = input('Entrez votre nom svp !\n'))

action = int(input('Pour Crediter votre compte : Entrez 1\nPour Debiter votre compte : Entrez 2\nPour Afficher votre compte : Entrez 3\n'))

if action == 1 :
   mon_compte.Crediter(int(input('entrez le montant a crediter ! \n'))) 
elif action == 2 :
    mon_compte.Debiter(int(input('entrez le montant a debiter ! \n')))
else :
    mon_compte.Afficher
    print(mon_compte)

