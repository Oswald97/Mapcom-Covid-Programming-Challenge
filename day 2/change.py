import sys

f = sys.stdin

n = int(f.readline().strip())

for i in range(n):
    amount = int(f.readline().strip())
    q = amount//25
    d = (amount-q*25)//10
    n = (amount -q*25-d*10)//5
    p = (amount -q*25-d*10-n*5)
    print(i+1,q,"QUARTER(S),", d,"DIME(S),",n,"NICKEL(S),",p,"PENNY(S)")
