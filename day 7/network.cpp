#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;
const int N=1e4+10;
vector<int> G[N];
int d,q;

void search(int u,int v,int cur){
    if(d<cur){
        d=cur;
        q=v;
      }
    for(int i=0;i < G[v].size();i++){
        if(u!=G[v][i]){
            search(v,G[v][i],cur+1);
        }
    }
}

int main()
{
    int t,a,b,n;
    ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
    cin>>t;
    while(t--){
        cin>>n;
        for(int i=1;i<=n;i++) G[i].clear();
        for(int i=1;i<n;i++){
            cin>>a>>b;
            G[a].push_back(b);
            G[b].push_back(a);
        }
        d=0;
        search(0,1,0);
        d=0;
        search(0,q,0);
        cout<<n-1-d<<endl;
    }
    return 0;
}
