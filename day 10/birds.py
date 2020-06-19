from collections import defaultdict
dic = {}
dic = defaultdict(lambda:[],dic)


n,m,t = map(int,input().strip().split(' '))
for i in range(m):
    a,b = map(int,input().strip().split(' '))
    dic[a].append(b)


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

dic = dict(dic)

final = []
for elem in dic.keys():
    path = find_all_paths(dic,elem,t)
    if len(path) ==1 and len(path[0])==2:
        final.append(elem)

print(len(final))
if len(final) == 0:
    pass
else:
    for elem in final:
        print(elem)
