from sys import stdin

f = stdin

p = int(f.readline())

for i in range(p):
    k,n = map(int,f.readline().split(' '))
    print(k,n*(n+1)//2,n*n,n*(n+1))
