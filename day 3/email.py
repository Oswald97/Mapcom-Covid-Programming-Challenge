
def is_username(name):
    if name=='' or name[0] == '.' or name[-1] == '.' :
        return False
    if name.find('..') != -1 or name.find('-') != -1:
        return False
    if len(name.replace('.',''))<6 or len(name.replace('.','')) >30:
        return False
    return True


def is_domaine(domaine):

    if domaine == '' or domaine[0] == '.' or domaine[-1] =='.' :
        return False
    if len(domaine) <3 or len(domaine)> 30:
        return False
    if domaine.find('_') !=-1:
        return False

    if any(len(part) ==0 for part in domaine.split('.')):
        return False
    return True

import sys
f = sys.stdin

p = int(f.readline().strip())

for i in range(p):
    valid = []

    n = int(f.readline().strip())

    for k in range(n):
        name,domaine = f.readline().strip().split("@")
        if is_username(name) and is_domaine(domaine):
            valid.append(name.replace('.','').lower()+'@'+domaine.lower())
    print(valid)
    print(len(set(valid)))
