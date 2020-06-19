tab = []
for i in range(16):
    a,b,c = map(int,input().strip().split(' '))
    tab.append((a,b,c))


def min_distance(tab,A):
    dis = float('inf')
    ans = None
    distance =0
    for elem in tab:
        distance = ((elem[0] - A[0])**2 + (elem[1] - A[1])**2 + (elem[2] - A[2])**2 )**0.5

        if distance < dis:
            ans = elem
            dis = distance

    return ans

a,b,c = map(int,input().strip().split(' '))
new = (a,b,c)


while new != (-1,-1,-1):
    ans = min_distance(tab,new)
    print('('+str(new[0])+','+str(new[1])+','+str(new[2])+ ')' + " maps to "+'('+str(ans[0])+','+str(ans[1])+','+str(ans[2])+ ')' )

    a,b,c = map(int,input().strip().split(' '))
    new = (a,b,c)
