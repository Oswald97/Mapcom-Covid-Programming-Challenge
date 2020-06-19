n,c,d = map(int,input().split(" "))
a,b = min(c,d),max(c,d)
stations = list(map(int,input().strip().split(" ")))
stations.sort()
min = 0
for i in range(n):
    if n==1:
        min = -1
        break
    else:
        if i != 0:
            if i != n-1:
                if (stations[i] - stations[i-1]) <= a:
                    if (stations[i+1] - stations[i]) <=a:
                        min += a

                    elif (stations[i+1] - stations[i]) <=b:
                        min += b

                    else:
                        min = -1
                        break
                elif (stations[i] - stations[i-1]) <= b:
                    if (stations[i+1] - stations[i]) <=b:
                        min += b
                    else:
                        min = -1
                        break
                else:
                    min = -1
                    break
            else:

                if (stations[i] - stations[i-1]) <= a:
                    min +=a
                elif (stations[i] - stations[i-1]) <= b:
                    min += b
                else:
                    min = -1
                    break

        else:
            if (stations[1] - stations[0]) <=a:
                min += a

            elif (stations[1] - stations[0]) <=b:
                min += b

            else:
                min = -1
                break


print(min)
