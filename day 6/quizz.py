def findmax(n , m ):
    oper = arr[0] ;

    for i in range(n,n+m+1):
       oper = oper | arr[i]

    print(oper)




from sys import stdin

f = stdin

p = int(f.readline())

for i in range(p):
    n,m = map(int,f.readline().split(' '))
    arr = list(map(int,f.readline().split(' ')))

    ans = arr[0]

    for i in range(2,n+m+1):
        if(n):
            ans &= arr[i]
            n -=1
        else:
            ans = ans | arr[i]

    print(ans)
