# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=16&reg_typ_id=2&que_str_id=&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D18#

import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
maxi = 1

for line in lines[1:]:
    if len(line) > maxi:
        maxi = len(line)
        
print(maxi)

#autre version inline

print(max(len(x) for x in lines[1:]))