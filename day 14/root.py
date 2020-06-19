n = int(input().strip())
while n !=0:
    while len(str(n)) != 1:
        n = sum(int(i) for i in str(n))
    print(n)
    n = int(input().strip())
