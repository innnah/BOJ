#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

const int MAX = 1000000;
const int INF = 987654321;
int dp[MAX+5][2];
int nums[3] = { 3, 5, 8 };
int t, n;
int main() {
	fastio;
	for (int i = 1; i <= MAX; i++) {
		dp[i][0] = INF;
	}
	for (int i = 3; i <= MAX; i++) {
		for (auto& j : nums) {
			if (i >= j) {
				if (dp[i - j][0] + 1 < dp[i][0]) {
					dp[i][0] = dp[i - j][0] + 1;
					dp[i][1] = j;
				}
			}
		}
	}
	cin >> t;
	while (t--) {
		cin >> n;
        if (dp[n][0] == INF) {
            cout << -1 << endl;
            continue;
        }
		while (n != 0) {
			cout << dp[n][1];
			n -= dp[n][1];
		}
		cout << endl;
	}
	return 0;
}