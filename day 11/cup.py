from collections import defaultdict

def sort(x):

    return [(k,v) for k, v in sorted(x.items(), key=lambda item: item[1], reverse =True)]


t = int(input().strip())



for i in range(t):
    points = defaultdict(lambda:0,{})
    n =int(input().strip())
    for j in range((n-2)*(n//2)):
        a,b,c = input().strip().split(' ')
        a,b = int(a),int(b)
        if c == 'W':
            points[a] +=3
        elif c == 'L':
            points[b] +=3
        elif c == 'D':
            points[a] += 1
            points[b] +=1

    result = ['0']*(n)

    points = sort(dict(points))
    k,v = points[0]
    result[k-1] = '1'
    points.pop(0)
    k,v = points[0]
    result[k-1] = '1'
    points.pop(0)

    for elem in points:
        c,d = elem
        if d+3 >=v:
            result[c-1] = '1'
    print("".join(result))
