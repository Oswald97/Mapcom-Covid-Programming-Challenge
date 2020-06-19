
tab = [0,2,4,6,8,1,3,5,7,9]

n = input().replace(" ","").strip()

while n != "0000000000000000":

    ans =0
    for j,i in enumerate(n):
        if (j+1)%2 !=0:
            ans += tab[int(i)]
        else:
            ans += int(i)
    if ans%10 == 0:
        print("Yes")
    else:
        print("No")
    n = input().replace(" ","").strip()
