#include <bits/stdc++.h>
using namespace std;
const int MOD = 1000000007;
int n, arr[10001], dp[10001][5001];
int dpf(int idx, int height) {
    if (idx == n-1) {
        return height == 0;
    }
    if (height > min(idx, n-1-idx) || height < 0) return 0;
    if (arr[idx] != -1 && arr[idx] != height) return 0;
    int& ret = dp[idx][height];
    if (ret != -1) return ret;
    ret = 0;
    ret += dpf(idx+1, height+1);
    ret %= MOD;
    ret += dpf(idx+1, height);
    ret %= MOD;
    ret += dpf(idx+1, height-1);
    ret %= MOD;
    return ret;
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    memset(dp, -1, sizeof(dp));
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        if (arr[i] > min(i, n-1-i)) {
            cout << 0;
            return 0;
        }
    }
    cout << dpf(0, 0);
    return 0;
}