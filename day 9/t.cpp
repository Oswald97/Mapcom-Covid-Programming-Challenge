#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<iostream>
using namespace std;
const int inf=0x3f3f3f3f;
char s[105][105];
int t[105][105];
int vis[105][105];
int fx[]={1,-1,0,0,1,1,-1,-1};
int fy[]={0,0,1,-1,1,-1,1,-1};
int px[]={1,-1,0,0};
int py[]={0,0,1,-1};
int n,m,k,sx,sy;
struct node
{
    int x,y,step;
}r,p,q;
queue<node> Q;
void bfs_fire()
{
    int i;
    while(!Q.empty())
    {
        p=Q.front();
        Q.pop();
        for(i=0;i<8;i++)
        {
            q=p;
            q.x+=fx[i];
            q.y+=fy[i];
            q.step+=k;
            if(q.x<0||q.y<0||q.x>=n||q.y>=m)
                continue;
            if(vis[q.x][q.y]==0)
            {
                vis[q.x][q.y]=1;
                t[q.x][q.y]=q.step;
                Q.push(q);
            }
        }

    }
}
int bfs_people()
{
    while(!Q.empty())
        Q.pop();
    cout <<vis[5][0]<<endl;
    memset(vis,0,sizeof(vis));
    cout<<vis[5][0]<<endl;
    int i;
    p.x=sx;
    p.y=sy;
    p.step=0;
    vis[p.x][p.y]=1;
    Q.push(p);
    while(!Q.empty())
    {
        p=Q.front();
        Q.pop();
        //printf("%d %d\n",p.x,p.y);
        if(s[p.x][p.y]=='t')
            return p.step;
        for(i=0;i<4;i++)
        {
            q=p;
            q.x+=px[i];
            q.y+=py[i];
            q.step++;
            if(q.x<0||q.y<0||q.x>=n||q.y>=m)
                continue;
            if(vis[q.x][q.y]==0&&q.step<t[q.x][q.y])
            {
                vis[q.x][q.y]=1;
                Q.push(q);
            }
        }
    }
    return -1;
}

int main()
{
    int i,j;
    while(scanf("%d %d %d",&n,&m,&k)!=EOF)
    {
        if(n==0&&m==0&&k==0) break;
        memset(t,inf,sizeof(t));
        memset(vis,0,sizeof(vis));
        while(!Q.empty())
            Q.pop();
        for(i=0;i<n;i++)
        {
            scanf("%s",s[i]);
            for(j=0;j<m;j++)
            {
                if(s[i][j]=='f')
                {
                    r.x=i;
                    r.y=j;
                    r.step=0;
                    t[i][j]=0;
                    vis[i][j]=1;
                    Q.push(r);
                }
                if(s[i][j]=='s')
                {
                    sx=i;
                    sy=j;
                }
            }
        }
        bfs_fire();
        int ans=bfs_people();
        if(ans==-1) printf("Impossible\n");
        else printf("%d\n",ans);

    }
  }
