#include <bits/stdc++.h>
using namespace std;

int n, l[51], dp[51][1000010];
int dpf(int idx, int d) {
    if (idx == n) {
        if (d == 0) {
            return 0;
        }
        return -987654321;
    }
    int& ret = dp[idx][d+500000];
    if (ret != -1) return ret;
    ret = max(dpf(idx + 1, d), dpf(idx + 1, d + l[idx]) + l[idx]);
    ret = max(ret, dpf(idx + 1, d - l[idx]));
    if (ret < 0) return ret = -987654321;
    return ret;
}

int main() {
    cin >> n;
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < n; ++i) cin >> l[i];
    dpf(0, 0);
    int ret = dp[0][500000];
    if (ret <= 0) cout << -1;
    else cout << ret;
    return 0;
}