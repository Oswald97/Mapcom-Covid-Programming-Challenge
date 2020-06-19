from collections import defaultdict

def sort(x):

    return [v for k, v in sorted(x.items(), key=lambda item: item[1])]


t = int(input().strip())

for i in range(t):
    files = defaultdict(lambda:1000000,{})
    n = int(input().strip())
    for j in range(n):
        name,id = input().strip().split(" ")
        id = int(id)
        files[name] = min(files[name],id)

    files = sort(dict(files))

    ans =''

    for id in files:
        ans += str(id) + ' '

    print(ans.strip())
