#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
const int MAX = 16;
int n, k, h[MAX];
ll cache[MAX][1 << MAX];
ll dp(int here, int visited) {
    if (visited == (1 << n) - 1) return 1;
    ll& ret = cache[here][visited];
    if (ret >= 0) return ret;
    ret = 0;
    for (int i = 0; i < n; ++i) {
        if ((visited & (1 << i)) || abs(h[i] - h[here]) <= k) continue;
        ret += dp(i, visited + (1 << i));
    }
    return ret;
}
int main() {
    fastio;
    memset(cache, -1, sizeof(cache));
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }
    ll ret = 0;
    for (int i = 0; i < n; ++i) {
        ret += dp(i, (1 << i));
    }
    cout << ret << endl;
    return 0;
}