#include <bits/stdc++.h>
using namespace std;
const long long INF = 98765432123456789;
int n, arr[501], psum[501];
long long dp[501][501];
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; ++i) cin >> arr[i];
        psum[1] = arr[0];
        for (int i = 2; i <= n; ++i) psum[i] = psum[i-1] + arr[i-1];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) {
                if (i == j) dp[i][j] = 0;
                else dp[i][j] = INF;
            }
        for (int s = 0; s < n; ++s)
            for (int i = 0; i < n-s; ++i) {
                int j = i+s;
                for (int k = i; k < j; ++k)
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + psum[j+1] - psum[i]);
            }
        cout << dp[0][n-1] << "\n";
    }
    return 0;
}