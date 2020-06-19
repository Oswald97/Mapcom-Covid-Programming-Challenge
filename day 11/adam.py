t = int(input().strip())
for i in range(t):
    c = input().strip()
    a = c.find('D')

    if a == -1:
        print(len(c))
    else:
        print(a)
