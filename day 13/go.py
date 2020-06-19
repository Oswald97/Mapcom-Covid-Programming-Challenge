n = int(input().strip())


for i in range(n):
    is_start_by_zero = False
    nb_zero = 0
    ans = True

    str_nb = input().strip()

    int_nb = int(str_nb)

    if len(str_nb) != len(str(int_nb)):
        is_start_by_zero = True
        nb_zero = len(str_nb) - len(str(int_nb))

    if is_start_by_zero:
        for j in range(2,len(str_nb)+1):
            temp = int_nb * j
            if nb_zero != str(temp).count('0'):
                ans = False
                break
            elif any(str(temp).count(str(k)) != str_nb.count(str(k))  for k in range(1,10)):
                ans = False
                break

    else:
        s = len(str_nb)//2
        for j in range(1,len(str_nb)+1):
            temp = str(int_nb * j)
            sub = temp[s:]
            if any(str(temp).count(str(k)) != str_nb.count(str(k))  for k in range(10)):
                ans = False
                break

    if ans:
        print(str_nb + ' is cyclic')
    else:
        print(str_nb + ' is not cyclic')
