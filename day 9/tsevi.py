from collections import deque

inf=float('inf');
s = [[0]*105]*105
t = [[inf]*105]*105
vis = [[0]*105]*105
fx=[1,-1,0,0,1,1,-1,-1]
fy=[0,0,1,-1,1,-1,1,-1]
px=[1,-1,0,0]
py=[0,0,1,-1]
n,m,k,sx,sy =0,0,0,0,0

class Node():
    def __init__(self,x,y,step):
        self.x=x
        self.y=y
        self.step=step

r,p,q = None,None,None

Q = deque()


def bfs_fire():
    global vis

    while(Q):
        p=Q.popleft()

        for i in range(8):
            q = p
            q.x+=fx[i]
            q.y+=fy[i]
            q.step+=k
            if q.x<0 or q.y<0 or q.x>=n or q.y>=m:
                continue

            if vis[q.x][q.y]==0:

                vis[q.x][q.y]=1
                t[q.x][q.y]=q.step
                Q.append(q)

def bfs_people():

    while Q:
        Q.popleft()

    global vis
    vis = [[0]*105]*105

    p = Node(sx,sy,0)
    vis[p.x][p.y]=1
    Q.append(p)
    while(Q):

        p= Q.popleft()

        if s[p.x][p.y]=='t':
            return p.step

        for i in range(4):
            q=p
            q.x+=px[i]
            q.y+=py[i]
            q.step +=1
            if q.x<0 or q.y<0 or q.x>=n or q.y>=m:
                continue

            if vis[q.x][q.y]==0 and q.step<t[q.x][q.y]:
                vis[q.x][q.y]=1
                Q.append(q)
    return -1



while(True):

    n,m,k = map(int,input().split(' '))
    if n==0 and m==0 and k==0:
        break
    t = [[inf]*105]*105
    vis = [[0]*105]*105
    Q.clear()
    for i in range(n):

        s[i] = input().strip()
        for j in range(m):

            if(s[i][j]=='f'):
                r = Node(i,j,0)
                t[i][j]=0
                vis[i][j]=1
                Q.append(r)

            if s[i][j]=='s':
                sx=i
                sy=j


    bfs_fire()
    ans=bfs_people()

    if ans == -1:
        print("Impossible")
    else:
        print(ans)
