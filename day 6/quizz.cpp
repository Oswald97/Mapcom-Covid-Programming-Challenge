#include <bits/stdc++.h>
using namespace std;
typedef long  long int ll;
const int N = 2e4 +10;

int p[N];

int main()
{
    int n, t, a, b;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &a, &b);
        n = a + b + 1;
        for(int i = 1; i <= n; ++i)
        {
            scanf("%d", &p[i]);
        }
        ll ans = p[1];
        for(int i = 2; i <= n; ++i)
        {
            if(a)
            {
                ans &= p[i];
                a--;
            }
            else
            {
                ans |= p[i];
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
