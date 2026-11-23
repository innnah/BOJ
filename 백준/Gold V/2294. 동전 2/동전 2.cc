#include <bits/stdc++.h>

using namespace std;

int n, k, dp[10005], coins[105];
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> coins[i];
    }
    for (int i = 1; i <= k; ++i) {
        dp[i] = 987654321;
        for (int j = 0; j < n; ++j) {
            if (i - coins[j] < 0) continue;
            dp[i] = min(dp[i], dp[i-coins[j]]+1);
        }
    }
    if (dp[k] == 987654321) cout << -1;
    else cout << dp[k];
    return 0;
}