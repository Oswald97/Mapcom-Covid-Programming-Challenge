
fac = [(30,40),(35,30),(40,20)]

c,d = map(int,input().split(" "))
while (c,d) != (0,0):
    min_facturation = min([f[0]*c+f[1]*d for f in fac])
    print(min_facturation)
    c,d = map(int,input().split(" "))
