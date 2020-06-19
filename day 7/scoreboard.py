from collections import defaultdict

values = tuple(map(int, input().strip().split(" ")))

while(values != (0,0,0)):

    T, P, S = values
    accepted = list()
    for _ in range(S):
         values = input().strip().split(" ")
         if len(values)==4:
             accepted.append(values)

    accepted.sort(key = lambda s: list(map(int,s[2].split(":"))))

    start, end = "--:--:--","--:--:--"

    is_ideal = False

    psbt = defaultdict(set)
    twsp = defaultdict(set)
    tslo = set()
    tsa = set()
    pslo = set()
    psa = set()

    for param in accepted:
         id, problem, time, ans = param
         psbt[id].add(problem)
         twsp[problem].add(id)
         tslo.add(id)
         if len(psbt[id]) == P:
             tsa.add(id)
         pslo.add(problem)
         if len(twsp[problem]) == T:
             psa.add(problem)
         submission_is_ideal = len(tslo) == T and len(tsa)==0 and len(pslo) == P and len(psa)==0
         if is_ideal:
             if not submission_is_ideal:
                 is_ideal, end = False, time
                 break
         else:
             if submission_is_ideal:
                 is_ideal, start = True, time
    print(start,end)

    values = tuple(map(int, input().strip().split(" ")))
