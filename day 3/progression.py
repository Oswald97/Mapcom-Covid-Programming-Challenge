import sys

f = sys.stdin

line = f.readline().strip()

while line != '0 0 0':
    a,b,c = map(int,line.split(" "))

    if c-b == b-a:
        print("AP",2*c-b)
    else:
        if a != 0:
            print("GP",c*(b//a))
        else:
            print("GP",c*(c//b))

    line = f.readline().strip()
