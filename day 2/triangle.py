

import sys

f= sys.stdin
line = f.readline().strip()
dic = {}
while line != '#':
    if line == '*':
        pass

    for i in range(6):
        dic[i] = f.readline().strip().split(" ")
