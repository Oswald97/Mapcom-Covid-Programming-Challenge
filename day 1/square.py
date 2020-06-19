import sys

def recursive_cuntor(n):
    return int((n*(n+1)*(2*n+1))/6)

f = sys.stdin
# p = Number of test cases
p = int(f.readline())
for i in range(p):
    print(recursive_cuntor(int(f.readline())))
