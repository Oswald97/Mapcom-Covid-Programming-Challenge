def conserve(k):
    pass

def sell(amount,q,price):
    amount = q *price
    q = 0
    return amount,q



def buy(amount,q,price):
    q = amount/price
    amount = 0
    return amount,q

t = int(input().strip())
for i in range(t):
    q = 1
    amount = 0

    n = int(input().strip())
    prices =list(map(int,input().strip().split(' ')))
    for j in range(n-1):
        if q == 0:
            amount,q = buy(amount,q,prices[j])

        if prices[j] > prices[j+1]:
            amount,q = sell(amount,q,prices[j])

    if q == 0:
        print('%.6f' % amount)
    else:
        print('%.6f' % (q*prices[-1]))
