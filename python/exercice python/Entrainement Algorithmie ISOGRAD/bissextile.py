# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=10&reg_typ_id=2&que_str_id=&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D82#


import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
    
for line in lines[1:]:
    if (int(line) % 4 == 0 and int(line) % 100 != 0) or (int(line) % 400 == 0):
        print("BISSEXTILE")
    else:
        print("NON BISSEXTILE")