#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

typedef int cache_type;
const int MAX = 16;
const int INF = 987654321;
int n, p;
int c[MAX][MAX];
string broken;
cache_type cache[MAX][1 << MAX];
cache_type dp(int here, int visited) {
    if (__builtin_popcount(visited) >= p) return 0;
    cache_type& ret = cache[here][visited];
    if (ret >= 0) return ret;
    ret = INF;
    for (int i = 0; i < n; ++i) {
        if (visited & (1 << i)) continue;
        int newState = visited + (1 << i);
        for (int j = 0; j < n; ++j) {
            if (newState & (1 << j))
                ret = min(ret, c[here][i] + dp(j, newState));
        }
    }
    return ret;
}
int main() {
    fastio;
    memset(cache, -1, sizeof(cache));
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> c[i][j];
        }
    }
    cin >> broken;
    int start = 0;
    for (int i = 0; i < n; ++i) {
        if (broken[i] == 'Y') start += 1 << i;
    }
    cin >> p;
    if (p == 0) {
        cout << 0;
        return 0;
    }
    int ret = INF;
    for (int i = 0; i < n; ++i) {
        if (start & (1 << i)) ret = min(ret, dp(i, start));
    }
    if (ret == INF) cout << -1;
    else cout << ret;
    return 0;
}