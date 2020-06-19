import sys

f = sys.stdin

t = int(f.readline().strip())

for i in range(t):
    n = int(f.readline().strip())
    k = int(f.readline().strip())

    cap = 60+k

    if n <= cap:
        print(1500*n)
    else:
        print(1500*cap + 3000*(n-cap))
