n = int(input().strip())
tab =[]
if n == 0:
    print(0)
else:
    for i in range(n):
        x = int(input().strip())
        if x < 0 or len(str(x))>7:
            continue
        else:
            tab.append(x)
    tab = sorted(list(set(tab)))

    for i in range(len(tab)):
        if i < tab[i]:
            i -=1
            break
    print(i+1)
