import random

p1 = ["1"]
p2 = ["2"]
p3 = ["3"]
p4 = ["4"]
p5 = ["5"]
p6 = ["6"]

for i in range(9):
    p1.append("-")
    p2.append("-")
    p3.append("-")
    p4.append("-")
    p5.append("-")
    p6.append("-")

termine = False

while not termine:# ==> while termine == False
    pos1 = p1.index("1") #.index recupère l'index de "1"
    pos2 = p2.index("2")
    pos3 = p3.index("3")
    pos4 = p4.index("4")
    pos5 = p5.index("5")
    pos6 = p6.index("6")

    d1 = random.randint(1,10)
    d2 = random.randint(1,10)
    d3 = random.randint(1,10)
    d4 = random.randint(1,10)
    d5 = random.randint(1,10)
    d6 = random.randint(1,10)

    if d1 != 4 and d1 != 6:
        p1[pos1] = "-"
        p1[pos1 + 1] = "1"
    if d2 != 4 and d2 != 6:
        p2[pos2] = "-"
        p2[pos2 + 1] = "2"
    if d3 != 4 and d3 != 6:
        p3[pos3] = "-"
        p3[pos3 + 1] = "3"
    if d4 != 4 and d4 != 6:
        p4[pos4] = "-"
        p4[pos4 + 1] = "4"
    if d5 != 5 and d5 != 6:
        p5[pos5] = "-"
        p5[pos5 + 1] = "5"
    if d6 != 6 and d6 != 6:
        p6[pos6] = "-"
        p6[pos6 + 1] = "6"

    if p1[9] != "-" or p2[9] != "-" or p3[9] != "-" or p4[9] != "-" or p5[9] != "-" or p6[9] != "-":
        termine = True

    print(p1,p2,p3,p4,p5,p6, sep="\n")
    input()
    print("-----------------")
    print("-----------------")
