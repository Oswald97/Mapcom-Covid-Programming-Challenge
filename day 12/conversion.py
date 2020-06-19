def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    elif c>= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 10
    else:
        return ord(c) - ord('a') + 36

def toDeci(str,base):
    llen = len(str)
    power = 1
    num = 0
    for i in range(llen - 1, -1, -1):

        # A digit in input number must
        # be less than number's base
        if val(str[i]) >= base:
            print('Invalid Number')
            return -1
        num += val(str[i]) * power
        power = power * base
    return num


def toStr(n,base):
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

n = int(input().strip())

for i in range(n):
    a,b,str = input().strip().split(' ')
    print(a + " " + str)
    print(b + " "+ toStr(int(toDeci(str,int(a))),int(b)) + '\n')
