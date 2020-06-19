import sys

f = sys.stdin

p = int(f.readline().strip())

def conserve(k):
    pass

def sell(k,tab,r,q):
    c = q * tab[k] + r
    q = 0
    r = 0
    return c,q,r


def buy(k,tab,c):

    q = c//tab[k]
    r = c - q* tab[k]
    c = 0
    return c,q,r

for i in range(p):
    c,n = map(int,f.readline().strip().split(" "))
    tab, r ,q= [],0,1
    for j in range(n):
        tab.append(int(f.readline().strip()))
    tab.append(0)
    for k in range(n):
        if k == 0:
            c,q,r = buy(k,tab,c)

        if q == 0:
            c,q,r = buy(k,tab,c)
            if r > tab[k]:
                q += r//tab[k]
                r = r - q*tab[k]

        if tab[k] > tab[k+1]:
            c,q,r = sell(k,tab,r,q)

    print(c)
