# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=14&reg_typ_id=2&que_str_id=&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D13#

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    

print(lines)
    
total = 0
nb_jours = int(lines[0])

for prod in range(1, nb_jours):
    a = int(lines[prod])
    total = total + a

#autre methode
for prod in lines[1:]:
    total = total + int(prod)
    
print(total)

#autre methode
print(sum(int(prod) for prod in lines[1:]))
