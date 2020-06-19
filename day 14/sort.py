line = input().strip()
digits = '-0123456789'

while line != '.':
    line = line.replace('.','')
    line = line.split(', ')
    n = len(line)
    numbers = []
    words = []
    number_position = [False]*n

    for i,elem in enumerate(line):
        if elem[0] in digits:
            numbers.append(int(elem))
            number_position[i] = True

        else:
            words.append(elem)
    numbers.sort()
    words.sort()
    words = [v for v in sorted(words, key=lambda item: item.lower())]

    for i in range(n-1):
        if number_position[i]:
            print(numbers.pop(0), end=', ')
        else:
            print(words.pop(0), end=', ')

    if number_position[-1]:
        print(str(numbers.pop(0))+'.')
    else:
        print(words.pop(0) +'.')
    line = input().strip()
