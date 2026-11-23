#include <bits/stdc++.h>
#define ll long long
#define MOD 1000000009

using namespace std;

int n, k;
ll dp[1000005][7];
int main() {
    cin >> n >> k;
    dp[0][0] = 1;
    for (int i = 1; i <= n; i++){
        dp[i][0] = dp[i-1][0] * (k-1);
        for (int j = 1; j < 7; j++){
            dp[i][0] += dp[i-1][j] * (k-2);
        }
        dp[i][1] = dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5];
        dp[i][2] = dp[i-1][1];
        dp[i][3] = dp[i-1][2];
        dp[i][4] = dp[i-1][3];
        dp[i][5] = dp[i-1][2] + dp[i-1][6];
        dp[i][6] = dp[i-1][5];
        for (int j = 0; j < 7; j++){
            dp[i][j] %= MOD;
        }
    }
    ll ret = 0;
    for (int i = 0; i < 7; ++i) {
        ret += dp[n][i];
    }
    cout << ret % MOD;
    return 0;
}