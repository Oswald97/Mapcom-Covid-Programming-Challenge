
from sys import  stdin

def is_valid(custumer_key,potential,m):
    for i in range(m):
        if custumer_key[i] < potential[i]:
            return False
    return True

f = stdin

line = f.readline().strip()




while line != "0 0":

    line = line.split(" ")

    m,n = int(line[0]) , int(line[1])
    custumer_key = list(map(int,f.readline().split(" ")))
    ans = 0
    for i in range(n):
        potential = list(map(int,f.readline().split(" ")))
        if is_valid(custumer_key,potential,m):
            ans +=1


    print(ans)

    line = f.readline().strip()
