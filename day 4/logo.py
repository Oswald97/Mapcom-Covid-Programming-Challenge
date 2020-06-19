from sys import  stdin

def sort(x):

    return [k for k, v in sorted(x.items(), key=lambda item: item[1][3])]

f = stdin

n = int(f.readline().strip())

while n != 0:

    dic = {i:[0,0,0,0] for i in range(107)}



    for i in range(n):
        score = list(map(int,f.readline().strip().split(" ")))
        d = score.pop(0)
        for j in range(d):
            dic[score[j]][j] +=1
            dic[score[j]][3] += (3-j)
    ()
    final = sort(dic)
    temp =[]
    temp.append(final[-1])
    for k in range(107):

        if dic[final[-1 -k]][3] == dic[final[-k-2]][3]:
            temp.append(final[-2 -k])
        else:
            break

    if len(temp) == 1:
        print(temp[0])
    else:

        max = dic[temp[0]][0]
        sol = [temp[0]]
        for i in range(1,len(temp)):
            if dic[temp[i]][0] > max:
                sol = []
                sol.append(temp[i])
                max = dic[temp[i]][0]

            elif dic[temp[i]][0] == max:
                sol.append(temp[i])

        if len(sol) == 1:
            print(sol[0])

        else:
            max = dic[sol[0]][1]
            sol2 = [sol[0]]
            for i in range(1,len(sol)):
                if dic[sol[i]][1] > max:
                    sol2 = []
                    sol2.append(sol[i])
                    max = dic[sol[i]][0]
                elif dic[sol[i]][1] == max:
                    sol2.append(sol[i])
            sol2.sort()
            text =str(sol2.pop(0))
            for elem in sol2:
                text+=' '
                text+= str(elem)
            print(text)


    n = int(f.readline().strip())
