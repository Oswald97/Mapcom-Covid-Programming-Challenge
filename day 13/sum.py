n = int(input().strip())
array = []


a = input().strip()
tab = []
while True:
    tab += list(map(int,a.split(' ')))
    try:
        a = input().strip()
    except EOFError:
        break

for i in range(n):
    array.append(tab[:n])
    del tab[:n]



print(array)
