#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
const int MAX = 20;
const int INF = 987654321;
int n;
int cost[MAX][MAX], cache[MAX][1 << MAX];
int dp(int here, int visited) {
    if (here == n) return 0;
    int& ret = cache[here][visited];
    if (ret >= 0) return ret;
    ret = INF;
    for (int i = 0; i < n; ++i) {
        if ((visited & (1 << i))) continue;
        int cand = cost[here][i] + dp(here+1, visited + (1 << i));
        ret = min(ret, cand);
    }
    return ret;
}
int main() {
    memset(cache, -1, sizeof(cache));
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> cost[i][j];
        }
    }
    int ret = INF;
    for (int i = 0; i < n; ++i) {
        ret = min(ret, dp(0, 0));
    }
    cout << ret << endl;
    return 0;
}