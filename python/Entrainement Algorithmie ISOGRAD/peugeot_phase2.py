# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=14&reg_typ_id=2&que_str_id=&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D13#

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
affiche = int(lines[0])

for line in lines[2:]:
    affiche -= int(line)

print(affiche)
    

#autre version inline

print(int(lines[0]) - sum(int(line) for line in lines[2:]))