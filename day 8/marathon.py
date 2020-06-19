def get_score(d):
    if d <=10:
        return 10
    elif d <=30:
        return 9
    elif d <=50:
        return 8
    elif d <=70:
        return 7
    elif d <= 90:
        return 6
    elif d <=110:
        return 5
    elif d <=130:
        return 4
    elif d <=150:
        return 3
    elif d <= 170:
        return 2
    elif d <= 190:
        return 1
    else:
        return 0


score = 0

n = int(input())
for i in range(n):
    x,y = map(int,input().split(" "))

    score += get_score((x**2 + y**2)**0.5)

print(score)
