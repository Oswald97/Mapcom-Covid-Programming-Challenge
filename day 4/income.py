from sys import  stdin

f = stdin

line = int(f.readline().strip())

while line != 0:

    if line <= 1000000:
        print(line)
    elif line <=5000000:
        print(int(0.9*line))
    else:
        print(int(0.8*line))

    line = int(f.readline().strip())
