# https://www.w3schools.com/python/python_regex.asp 

# https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=10&reg_typ_id=2&que_str_id=&rtn_pag=https%3A%2F%2Fwww.isograd-testingservices.com%2F%2FFR%2Fsolutions-challenges-de-code%3Fcts_id%3D82#

import sys
import re

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
print(lines)

mdp = re.compile("[a-zA-Z][0-9][a-zA-Z]{4}")
nbre = 0

for line in lines[1:]:
    if len(line) == 6 and mdp.match(line):
        nbre += 1
        
print(nbre)