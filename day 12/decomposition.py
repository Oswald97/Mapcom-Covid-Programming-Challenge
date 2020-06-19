a = [[None]*250]*250
for i in range(0,250):
    for j in range(0,250):
        if ((j > i / 2) and (j <= i)) or (i == 0):
            a[i][j] = 1

for i in range(2,250):
    for j in range(i//2,0,-1):
        a[i][j] = a[i-(2 * j)][j] + a[i][j + 1]


n=int(input().strip())
while(n != 0):
    print(n,a[n][1])
    n=int(input().strip())
