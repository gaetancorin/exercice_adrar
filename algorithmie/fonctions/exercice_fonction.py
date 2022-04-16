# #### Écrire une fonction f1 qui ne prend rien en entrée, et qui affiche 17 dans la console.

def f1():
    print(17)
f1()

# #### Écrire une fonction f2 qui ne prend rien en entrée, et qui retourne 17.

# def f2():
#     return 17

# ##### Utiliser la fonction f1 pour afficher 17 dans la console.

# # f1()

# ##### Utiliser la fonction f2 pour afficher 17 dans la console.

# # print(f2())

# ##### La fonction f2 a l'air moins pratique à utiliser. Quel intérêt pourrait-elle avoir par rapport à f1 ?

# # Faire des calculs sans l'afficher sur le terminal

# ##### Écrire une fonction f3 qui prend un nombre en entrée et qui affiche dans la console le double de ce nombre.

# def f3(a):
#     a = a*2
#     print(a)

# ##### Écrire une fonction f4 qui prend un nombre en entrée et qui retourne le double de ce nombre.

# def f4(a):
#     a = a*2
#     return a

# ##### Utiliser la fonction f3 pour écrire dans la console le double de 99.

# # f3(99)

# ##### Utiliser la fonction f4 pour écrire dans la console le double de 99.

# # print(f4(99))

# ##### Utiliser la fonction f4 pour stocker dans une variable appelée a le double de 99.

# a=f4(99)

# ##### Écrire une fonction f5 qui prend en entrée deux nombres et qui affiche dans la console la somme de ces deux nombres.

# def f5(a,b):
#     print(a+b)   


# ##### Écrire une fonction f6 qui prend en entrée deux nombres et qui retourne la somme de ces deux nombres.

# def f6(a,b):
#     return a+b

# ##### Utiliser la fonction f5 pour écrire dans la console la somme de 42 et 77.

# # f5(42,77)

# ##### Utiliser la fonction f6 pour écrire dans la console la somme de 42 et 77.

# # print(f6(42,77))

# ##### Utiliser la fonction f6 pour incrémenter la variable a de la somme de 42 et 77.

# a += f6(42,77)
# print(a)



# # Écrire une fonction f7 qui prend deux nombres en entrée et qui retourne le plus grand des deux.
# def f7(a,b):
#     if a<b:
#         return b
#     else:
#         return a
# # Écrire une fonction f8 qui prend trois nombres en entrée et qui retourne le plus grand des trois.


# def f77(a,b,c):
#     l = []
#     l.append(a)
#     l.append(b)
#     l.append(c)
#     l = sorted(l)
#     return(l[2])




# def f777(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>a:
#         return b
#     else:
#         return c




        
# # (Au moins deux versions possibles : sans utiliser f7, et en utilisant f7).
# def f7777(a,b,c):
#     return f7(f7(a,b),c)


# # Écrire une fonction f9 qui prend un nombre et un mot en entrée, et qui affiche dans la console ce mot ce nombre de fois.

# def f9(a,b):
#     for _ in range(a):
#         print(b)


# Fonction qui prend un tableau en entrée et affiche le dernier élément de ce tableau.

# def tableau1(l):
#     print(l[len(l)-1])

# a = tableau1([24,44,11,41,30])

# Fonction qui prend un tableau en entrée et retourne le dernier élément de ce tableau.

# def tableau2(l):
#     return l[len(l)-1]

# Fonction qui prend en entrée un tableau et qui retourne le minimum de ce tableau.



# def tableau1(l):
#     a = l[0]
#     for i in range(len(l)):
#         if a > l[i]:
#             a = l[i]
#         else:
#             pass
#     return a

# liste = [42,48,11,25,11]
# print(tableau1(liste))

# print(tableau1([24,44,11,41,2]))

# a = tableau1([24,44,11,41,2])
# print(a)

# Fonction qui prend en entrée un tableau et qui retourne le maximum de ce tableau.

# def tableau1(l):
#     a = l[0]
#     for i in range(len(l)):
#         if a < l[i]:
#             a = l[i]
#         else:
#             pass
#     return a


# ++ Fonction qui prend en entrée un tableau de nombres positifs et qui retourne la deuxième plus grande valeur du tableau.

# def tableau1(l):
#     a = l[0]
#     b = 0
#     for i in range(len(l)):
#         if a < l[i]:
#             b = a
#             a = l[i]
#             print('changement',a,b)
#         elif b < l[i]:
#             b = l[i]
#             print('changement',b)
#         else:
#             print('pass')
#             pass
#     return b

# a = tableau1([24,44,11,41,2])
# print(a)

# Fonction qui prend en entrée un tableau et un nombre et qui retourne le nombre de fois que ce nombre apparaît dans le tableau.

# def tableau1(l,b):
#     count = 0
#     for i in range(len(l)):
#         if l[i] == b:
#             count = count + 1
#         else:
#             pass
#     return count

# b = 11
# a = tableau1([24,44,11,41,11], b)
# print(a)


# Fonction qui prend en entrée un tableau et un nombre et qui retourne True si le nombre existe dans le tableau, False sinon.

# def tableau1(l,b):
#     count = 0
#     for i in range(len(l)):
#         if l[i] == b:
#             count = count + 1
#         else:
#             pass

#     if count > 0:
#         return 'true'
#     else:
#         return 'false'

# b = 11
# a = tableau1([24,44,11,41,4], b)
# print(a)

# Variante de l'exo : on **sait** que le tableau reçu est trié (on ne le vérifie pas). Comment exploiter cette information pour améliorer la recherche d'un élément ?