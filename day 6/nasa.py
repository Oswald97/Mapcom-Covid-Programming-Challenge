from sys import stdin

f = stdin

n = int(f.readline())
dictionnary ={}
for i in range(n):
    english,eq,minion = f.readline().strip().split(" ")
    dictionnary[english] = minion


n = int(f.readline())


for i in range(n):
    text = ''
    size = int(f.readline())
    words = f.readline().strip().split(" ")

    for j in range(size-1):
        text += dictionnary[words[j]]
        text += ' '
    text+= dictionnary[words[-1]]
    print(text)
