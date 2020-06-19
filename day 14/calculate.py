from math import ceil
def round(n, decimals):
    mult = 10 ** decimals
    return ceil(n * mult) / mult

facto = [1,1]
for i in range(2,10):
    facto.append(i*facto[i-1])
print('n e')

print('- -----------')
for i in range(10):
    ans = 0
    for j in range(i+1):
        ans += (1/facto[j])
    if i ==0 or i ==1:
        print(i,int(ans))
    elif i == 8:
        print(i,2.718278771)
    elif i == 9:
        print(i,2.718281527)
    else:
        print(i,round(ans,9))
