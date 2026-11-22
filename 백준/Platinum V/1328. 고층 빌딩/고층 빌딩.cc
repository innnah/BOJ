#include <bits/stdc++.h>
#define ll long long

using namespace std;

const ll MOD = 1000000007;
int n, a, b;
ll dp[101][101][101];
ll dpf(int idx, int left, int right) {
    if (idx == n) {
        return left == a && right == b;
    }
    ll& ret = dp[idx][left][right];
    if (ret != -1) return ret;
    ret = 0;
    if (left != a) ret += dpf(idx+1, left+1, right);
    ret %= MOD;
    if (right != b) ret += dpf(idx+1, left, right+1);
    ret %= MOD;
    ret += (idx-1) * dpf(idx+1, left, right);
    return ret % MOD;
}
int main() {
    cin >> n >> a >> b;
    memset(dp, -1, sizeof(dp));
    cout << dpf(1, 1, 1);
    return 0;
}