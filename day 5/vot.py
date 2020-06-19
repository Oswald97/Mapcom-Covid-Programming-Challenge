elec = []
need = 0
memo = []
inf = float('inf')

def sol(id, total):
    #id int
    #total int
    if(id == len(elec)):
        if(total >= need):
            return 1
        else:
            return 0

    ans = memo[id][total]
    if(ans != inf):
        return ans;

    ans = 0
    ans = elec[id][0] * sol(id + 1, total + elec[id][2])
    ans += (1 - elec[id][0]) * sol(id + 1, total)
    return ans
from sys import stdin

f = stdin
n = int(f.readline())

while n !=0:
    elec.clear()
    need = 0
    for i in range(n):
        line = f.readline().split(' ')
        p,e = float(line[0]),int(line[1])
        elec.append((p,e))
        need += e

    memo.clear()
    memo = [(need+10, inf) for i in range(n+1)]
    need /= 2
    need +=1

    print('%.4f' % sol(0, 0))

    n = int(f.readline())
