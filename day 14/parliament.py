
m, p, r = map(int, input().strip().split(" "))
while (m,p,r) != (0,0,0):

    vneed = (m//2)+1
    pneed = max(vneed-p,0)
    remain = m-p-r
    if pneed>remain:
        pneed = -1
    print(pneed)
    m, p, r = map(int, input().strip().split(" "))
