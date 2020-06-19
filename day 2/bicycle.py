import sys
PI = 3.1415927

f = sys.stdin
tab = f.readline().strip().split(' ')
i = 1

while int(tab[1]) != 0:
    diam,nb,t = float(tab[0]),int(tab[1]),float(tab[2])
    if  t <= 0:
        i+=1
        tab = f.readline().strip().split(' ')
        continue

    distance = nb*diam*PI/63360

    v = (distance*3600)/t
    print("Trip #"+str(i)+': %.2f' %distance+' %.2f' %v)
    i +=1
    tab = f.readline().strip().split(' ')
