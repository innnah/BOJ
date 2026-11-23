#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

typedef ll cache_type;
const int MAXM = 14;
const int MAXN = 50;
const int INF = 987654321;
int n, m;
int c[MAXN][MAXM];
ll sum[MAXM];
cache_type cache[1 << MAXM][MAXN];
cache_type dp(int here, int visited, int remain) {
    if (here == n) return 0;
    cache_type& ret = cache[visited][remain];
    if (ret >= 0) return ret;
    ret = INF;
    for (int i = 0; i < m; ++i) {
        if (visited & (1 << i)) continue;
        ret = min(ret, sum[i] - c[here][i] + dp(here + 1, visited + (1 << i), remain));
    }
    if (remain) ret = min(ret, dp(here + 1, visited, remain - 1));
    return ret;
}
int main() {
    fastio;
    memset(cache, -1, sizeof(cache));
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> c[i][j];
            sum[j] += c[i][j];
        }
    }
    cout << dp(0, 0, n-m);
    return 0;
}