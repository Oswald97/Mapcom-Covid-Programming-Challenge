from sys import stdin

f = stdin
t = int(f.readline().strip())

kilo = {1:1,2:3,3:5}

for i in range(t):
    g,c,e = map(int,f.readline().strip().split(' '))
    if c < e:
        print((e-c)*kilo[g])
    else:
        print(0)
