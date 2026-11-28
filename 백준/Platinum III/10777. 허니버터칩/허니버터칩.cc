#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, m, arr1[3027], arr2[127];
int dp[3005][105][105][2];
int dpf(int a, int b, int c, int p) {
    if (a == n && b >= c) return 0;
    int& ret = dp[a][b][c][p];
    if (ret != -1) return ret;
    if (b < c) {
        if (p) ret = max(ret, dpf(a, b, c-1, 0) + arr2[c-1]);
        ret = max(ret, dpf(a, b + 1, c, 1));
    }
    if (a < n) {
        if (p) ret = max(ret, dpf(a + 1, b, c, 0) + arr1[a]);
        ret = max(ret, dpf(a + 1, b, c, 1));
    }
    return ret;
}
int main() {
    fastio;
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> arr1[i];
    cin >> m;
    for (int i = 0; i < m; ++i) cin >> arr2[i];
    sort(arr2, arr2 + m);
    memset(dp, -1, sizeof(dp));
    cout << dpf(0, 0, m, 1);
    return 0;
}