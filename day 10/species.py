from collections import defaultdict
dic = {}
dic = defaultdict(lambda:0,dic)

def sort(x):

    return [(k,v) for k, v in sorted(x.items(), key=lambda item: item[1], reverse =True)]

n = int(input().strip())
for i in range(n):
    dic[input().strip()] +=1
dic = dict(dic)
dic = sort(dic)
sp,max = dic[0]
if max > n//2:
    print(sp)
else:
    print("NONE")
