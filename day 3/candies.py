import sys

f = sys.stdin

t = int(f.readline().strip())

for i in range(t):
    k = int(f.readline().strip().split(" ")[1])
    tab = list(map(int,f.readline().strip().split(" ")))
    happy =0
    for elem in tab:
        happy += elem//k
    print(happy)
