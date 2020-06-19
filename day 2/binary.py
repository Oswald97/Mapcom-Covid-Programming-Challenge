import sys

f = sys.stdin

n = int(f.readline().strip())

for i in range(n):
    a,b = f.readline().strip().split(' ')
    print(i+1,bin(int(a,2) + int(b,2)).split('b')[1])
