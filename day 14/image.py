n = int(input().strip())

digits = "123456789"
capital_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(n):
    is_good = True
    number = input().strip()

    if is_good and ((number[0] not in digits) or (number[0] != number[1])):
        is_good = False

    if is_good and ((number[2] not in digits) or (number[3] not in digits)):
        is_good = False

    if is_good and (number[4] not in capital_char):
        is_good = False
        
    if is_good and ((number[5] not in digits) or (number[6] not in digits) or (number[7] not in digits)):
        is_good = False


    if is_good:
        print(number)
