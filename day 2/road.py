import sys

f = sys.stdin
for _ in range(int(f.readline())):
    N, start, end = (f.readline().split())
    start_, end_, start, end = start, end, start.lower(), end.lower()
    N = int(N)
    links = {}
    for i in range(N):
        depart, arrive, time = f.readline().split()
        depart, arrive, time = depart.lower(), arrive.lower(), int(time)
        # print(depart, arrive, time)
        links[depart] = links.get(depart, [])
        links[depart].append((arrive, time))
        links[arrive] = links.get(arrive, [])
        links[arrive].append((depart, time))
    # print(links)
    fringe = [start]
    close = {}
    dist = {}
    dist[start] = 0
    findi = False
    while len(fringe) > 0:
        # print('fr:', fringe)
        # print('dist', dist)
        node = fringe.pop(0)
        if node == end:
            findi = True
            print(start_, end_, dist[end])
            break
        if not close.get(node, False):
            for child, time in links[node]:
                if dist.get(node, float('inf')) + time < dist.get(child, float('inf')):
                    dist[child] = dist[node] + time
                    fringe.append(child)
            close[node] = True
        fringe.sort(key=lambda k: dist.get(k, float('inf')))
    if not findi:
        pass
    # exit()
# print(f'Case {_+1}: {0}')
