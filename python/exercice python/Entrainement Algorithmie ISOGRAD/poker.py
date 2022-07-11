# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=9&reg_typ_id=2&que_str_id=&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D8

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
total = int(lines[0])    
    
for line in lines[2:]:
    element = line.split(" ")
    mise = int(element[0])
    gain = int(element[1])
    total = total - mise + gain
    
    #autre version
    elem = line.split()
    total = total - int(elem[0]) + int(elem[1])
    
    #autre version
    total = total - int(line.split()[0]) + int(line.split()[1])
    
print(total)
