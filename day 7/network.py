import sys
sys.setrecursionlimit(10500)
G = [[] for i in range(10500)]

q = 0
d = 0

def search(u,v,current):
    global d
    global q

    if d<current:
        d = current
        q = v

    for i in range(len(G[v])):
        if u != G[v][i]:
            search(v,G[v][i],current+1)


t = int(input())

for z in range(t):
    n = int(input())

    for i in range(1,n+1):
        G[i].clear()

    for i in range(1,n):
        a,b = map(int, input().split(" "))
        G[a].append(b)
        G[b].append(a)

    d = 0
    search(0,1,0)
    d = 0
    search(0,q,0)
    print(n-1-d)
