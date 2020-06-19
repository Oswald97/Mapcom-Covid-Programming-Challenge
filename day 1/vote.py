import sys


f = sys.stdin
def sort(x):

    return [k for k, v in sorted(x.items(), key=lambda item: item[1])]
# p = Number of test cases
p = int(f.readline())
for i in range(p):
    data = {}
    n,m = map(int,f.readline().strip().split(" "))
    for j in range(n):
        data[f.readline().strip()] = 0
    for k in range(m):
        candidat,nb,ville = f.readline().strip().split(" ")
        nb = int(nb)
        data[candidat] += nb

    rank = sort(data)

    if data[rank[-1]] == data[rank[-2]]:
        print("VOTE "+str(i+1)+": THERE IS A DILEMMA")
    else:
        print("VOTE "+str(i+1)+": THE WINNER IS "+rank[-1]+" "+ str(data[rank[-1]]))
