#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
const int MAX = 15;
const int INF = 987654321;
int n;
int cost[MAX][MAX], cache[MAX][1 << MAX][10];
int dp(int here, int visited, int price) {
    if (visited == (1 << n) - 1) return 0;
    int& ret = cache[here][visited][price];
    if (ret >= 0) return ret;
    ret = 0;
    for (int i = 0; i < n; ++i) {
        if ((visited & (1 << i)) || cost[here][i] < price) continue;
        int cand = 1 + dp(i, visited + (1 << i), cost[here][i]);
        ret = max(ret, cand);
    }
    return ret;
}
int main() {
    memset(cache, -1, sizeof(cache));
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < n; ++j) {
            cost[i][j] = tmp[j]-48;
        }
    }
    cout << dp(0, 1, 0)+1;
    return 0;
}