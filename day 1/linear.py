import sys


# n = Number of test cases
f = sys.stdin
n = int(f.readline().strip())
for i in range(n):
    tab = f.readline().strip().split(" ")
    a,b,c = map(int,[tab[0].split('x')[0],tab[2],tab[4]])

    print("Equation ",i+1)

    if a !=0 and (c-b) !=0:
        print("x = %.6f\n" % ((c-b)/a))
    elif a ==0 and (c-b)!=0 :
        print('No solution.\n')
    else:
        print("More than one solution.\n")
