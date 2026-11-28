#include <bits/stdc++.h>
using namespace std;

int n, dp[100001];
pair<int, int> arr[1127];

int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        cin >> n;
        int s = 0;
        for (int i = 0; i < n; ++i) {
            cin >> arr[i].first >> arr[i].second;
            s += arr[i].first;
        }
        for (int i = 1; i <= s; ++i) {
            dp[i] = 200000;
        }
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = s; j >= 0; --j) {
                dp[j] += arr[i].second;
                if (arr[i].first <= j) dp[j] = min(dp[j], dp[j-arr[i].first]);
            }
        }
        int ans = 200000;
        for (int i = 0; i <= s; ++i) {
            ans = min(ans, max(i, dp[i]));
        }
        cout << ans << endl;
    }
    return 0;
}