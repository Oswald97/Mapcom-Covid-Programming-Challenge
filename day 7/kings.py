line = input()
while line != '0 0 0 0':

    a,b,c,d = map(int,line.split(" "))
    print(abs(c-b),abs(d-a))
    line = input()
