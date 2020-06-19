from sys import stdin

f = stdin

p = int(f.readline())

for i in range(p):

    val = f.readline().split(' ')[1]
    try:
        oct = int(val,8)
    except ValueError:
        oct = 0

    print(i+1,oct,int(val),int(val,16))
