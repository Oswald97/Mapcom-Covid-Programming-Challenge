zh,ma = map(int,input().split(" "))
mh,za = map(int,input().split(" "))

if zh+za > ma+mh:
    print("Zamalek")
elif zh+za < ma+mh:
    print("Mazembe")
else:
    if za > ma:
        print("Zamalek")
    elif za < ma:
        print("Mazembe")
    else:
        print("Penalty")
