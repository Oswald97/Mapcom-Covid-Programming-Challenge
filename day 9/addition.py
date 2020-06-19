def retenu(a, b, e=0):
    x, r = a + b + e, 0
    if x >= 10:
        x -= 10
        r = 1
    return x,r

n = int(input())
while n != 0:
    a, b, c = list(map(int,input().rstrip())), list(map(int,input().rstrip())), list(map(int,input().rstrip()))
    linked,stop,temp = [0 for i in range(n)],n-1,[None for i in range(n)]
    for i in range(n):
        s, r = retenu(a[i], b[i])
        if s == c[i]:
            temp[i] = r
            linked[i] += 1
            stop = i

    for i in range(stop-1, -1, -1):
        for j in range(stop, i, -1):

            if temp[j] != None:
                sum, rem = retenu(a[i], b[i],temp[j])
                if sum == c[i] and linked[i] < linked[j] + 1:
                    linked[i] = linked[j] + 1
                    temp[i] = rem
    maxi = 0
    for i in range(n):
        if temp[i] == 0:
            maxi = max(maxi, linked[i])
    print(n - maxi)
    n = int(input())
