def area(X,Y,n):
    sum = 0
    for i in range(n):
        sum += (X[i]*Y[i+1] - Y[i]*X[i+1])
    return abs(sum)/2
n = int(input().strip())

total = 0
for i in range(n):
    X = []
    Y = []
    p = int(input().strip())
    for j in range(p):
        x,y = map(int,input().split(" "))

        X.append(x)
        Y.append(y)
    X.append(X[0])
    Y.append(Y[0])

    total += area(X,Y,p)

print(int(total))
