#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;
int n,k,x,y;
ll xx,z;
vector<ll> vt,t;
int main(){
    scanf("%d%d",&n,&k);
    for(int i=0;i<n;i++){
        scanf("%lld",&xx);
        vt.push_back(xx);
    }
    sort(vt.begin(),vt.end());
    t.assign(n,0);
    while(k--){
        scanf("%d%d%lld",&x,&y,&z);
        int it=x-1;
        int idx=0;
        for(int i=0;i<x-1;i++){
            while(it!=y&&vt[it]+z<=vt[i])
                t[idx++]=vt[it++]+z;
            t[idx++]=vt[i];
        }
        for(int i=y;i<n;i++){
            while(it!=y&&vt[it]+z<=vt[i])
                t[idx++]=vt[it++]+z;
            t[idx++]=vt[i];
        }
        while(it!=y)
            t[idx++]=vt[it++]+z;
        for(int i=0;i<n;i++)
            vt[i]=t[i];
    }
    for(auto next:vt)printf("%lld ",next);
    return 0;
}