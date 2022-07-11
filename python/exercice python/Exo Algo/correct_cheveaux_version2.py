import random

participants = int(input("indiquez le nombre de participant\n"))

field = []

for i in range(participants):
    field.append([i+1])
    for j in range(9):
        field[i].append("-")
print(field)

termine = False
# print(field)
while not termine:
    print("\n\nTOUR SUIVANT\n\n")
    j = 1
    for i in field:
        position = i.index(j)
        dice = random.randint(1,10)
        if dice != 4 and dice != 6:
            i[position] = "-"
            i[position + 1] = j
        print(i)
        if i[9] != "-":
            termine = True
        j += 1