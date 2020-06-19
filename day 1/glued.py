import sys

f = sys.stdin
a = f.readline().strip()
while a != '#':
    code = a.split(" ")[1]
    i=0
    val =''
    solutions = []
    while i < 3 and val != code[i]:


        if code[i] == code[i+1]:
            val = code[i]
            solutions.append(code[i])
            solutions.append(code[i+1])
            i+=1
        i +=1
    if len(solutions) == 2:
        print(solutions[0],solutions[1],'glued')
    elif len(solutions) == 4:
        print(solutions[0],solutions[1],'glued and',solutions[2],solutions[3],'glued')
    a = f.readline().strip()
