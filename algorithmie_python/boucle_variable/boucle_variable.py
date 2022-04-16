# Exercice 1 : écrire 50 fois "Bonjour" dans la console.

# for _ in range(50):
#     print('Bonjour')

# Exercice 2 : écrire dans la console :
# A
# B
# A
# B
# A
# B
# A
# B
# A
# B

# for _ in range(5):
#     print('A')
#     print('B')

# Exercice 3 : écrire dans la console :
# A
# A
# A
# A
# A
# B
# A
# A
# A
# A
# A
# B
# A
# A
# A
# A
# A
# B

# for _ in range(3):
#     for _ in range(5):
#         print('A')
#     print('B')

# Exercice 4 : écrire dans la console :
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# for i in range(10):
#     print(i)

# Exercice 5 : écrire dans la console :
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12

# n=3
# for _ in range(10):
#     print(n)
#     n += 1

# for i in range(3,13):
#     print(i)

# Exerice 6 : écrire dans la console :
# 0
# 1
# 2
# 3
# 0
# 1
# 2
# 3
# 0
# 1

# for _ in range(2):
#     for i in range(4):
#         print(i)
# print(0)
# print(1)

# a = 0
# for _ in range(10):
#     print(a)
#     a += 1
#     if a == 4:
#         a = 0


# Exercice 7 : écrire dans la console :
# 0
# 1
# 2
# 3
# 4
# A
# A
# A
# 8
# 9

# for i in range(5):
#     print(i)
# for _ in range(3):
#     print('A')
# print('8')
# print('9')

# for i in range(10):
#     if i == 5 or i == 6 or i == 7:
#         print('A')
#     else:
#         print(i)

# Exercice 8 : écrire dans la console :
# 100
# 1
# 2
# 103
# 4
# 5
# 106
# 7
# 8
# 109

# for a in range(10):
#     if a%3 == 0:
#         print(100 + a)
#     else:
#         print(a)
    

# Exercice 9 : écrire dans la console :
# 0
# 101
# 202
# 3
# 104
# 205
# 6
# 107
# 208
# 9

# for i in range(10):
#     if i%3 == 0:
#         print(i)
#     elif i%3 == 1:
#         print(i + 100)
#     else:
#         print(i + 200)

# Exercice 10 : écrire dans la console tous les résultats possibles de lancers de deux dé :
# 1 1
# 1 2
# 1 3
# ...
# 6 4
# 6 5
# 6 6

# for i in range(1,7):
#     for a in range(1,7):
#         print(a, i)

# Exercice 11 : adapter l'exercice précédent pour enlever les doublons (on ne veut pas afficher 1 2 et 2 1, mais seulement l'un des deux).

# for a in range(1,7):
#     for b in range(1,7):
#         if b >= a:
#             print(a, b)
#         else:
#             pass


# Exercice 12 : en prenant des dés à 20 faces, combien de résultats différents (sans doublon) peut-on afficher ? (Autrement dit : adapter le code précédent pour compter les résultats au lieu de les afficher)

# c = 0
# for a in range(1,21):
#     for b in range(a,21):
#         c += 1
# print(c)


# Exercice 13 : afficher la table de multiplication de 1 (de 1 à 9):
# 1x1 = 1
# 1x2 = 2
# 1x3 = 3
# 1x4 = 4
# 1x5 = 5
# 1x6 = 6 
# 1x7 = 7
# 1x8 = 8
# 1x9 = 9

# a = 1
# b = 1
# for _ in range(9):
#     print(a,'x',b, '=', a * b)
#     b += 1


# Exercice 14 : que faut-il modifier du code précédent pour obtenir la table de 2 :
# 2x1 = 2
# 2x2 = 4
# 2x3 = 6
# 2x4 = 8
# 2x5 = 10
# 2x6 = 12
# 2x7 = 14
# 2x8 = 16
# 2x9 = 18

# a = 2
# for b in range(1,10):
#     print(a,'x',b, '=', a * b)
#     b += 1

# Exercice 15 : comment généraliser pour afficher toutes les tables de multiplication de 1 à 9 :
# 1x1 = 1
# 1x2 = 2
# 1x3 = 3
# 1x4 = 4
# ...
# 9x7 = 63
# 9x8 = 72
# 9x9 = 81

# for a in range(10):
#     for b in range(10):
#         print(a,'x',b,'=',a*b)


# Exercice 16 : calculer 1+2+3+4+...+99+100. (Vous devriez trouver 5050)

# Exercice 17 : trouver le nombre n tel que 1+2+3+4+5+...+(n-1)+n = 302253

# Exercice 18 : Afficher :
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
