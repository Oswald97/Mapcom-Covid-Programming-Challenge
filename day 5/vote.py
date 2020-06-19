from sys import stdin

f = stdin
n = int(f.readline())

while n !=0:
    sum,total = 0,0
    c,i = 1,0
    tab = []
    for i in range(n):
        line = f.readline().split(' ')
        p,e = float(line[0]),int(line[1])
        total +=e
        tab.append((p,e))
    for elem in tab:
        p,e = elem
        if e > total/2:
            c = p
            i = 1.0
            sum = float('inf')
        if sum < total/2:
            sum += e
            c += p*e
            i +=e
        else:
            sum = float('inf')


    print('%.4f' % (c/i))

    n = int(f.readline())
