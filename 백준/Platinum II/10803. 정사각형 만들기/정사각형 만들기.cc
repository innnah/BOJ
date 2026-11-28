#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

int dp[1000][1000], n, m;
int dpf(int a, int b) {
    if (a < b) return dpf(b, a);
    if (a == b) return 1;
    if ((a / b) * b == a) return a / b;
    if (dp[a][b] != -1) return dp[a][b];
    int& ret = dp[a][b];
    ret = 987654321;
    for (int i = 1; i <= a / 2; ++i) {
        ret = min(ret, dpf(i, b) + dpf(a - i, b));
    }
    for (int i = 1; i <= b / 2; ++i) {
        ret = min(ret, dpf(a, i) + dpf(a, b - i));
    }
    return ret;
}
int main() {
    fastio;
    cin >> n >> m;
    if (n < m) swap(n, m);
    int ret = 0;
    if (n > m * 3) {
        ret += (n - m * 2) / m;
        n -= ret * m;
    }
    memset(dp, -1, sizeof(dp));
    cout << ret + dpf(n, m);
    return 0;
}