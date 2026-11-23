#include <bits/stdc++.h>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

int n, arr[2223][2223], dp[2223][2223];
inline bool isInside(int x, int y) { return 0 <= x && 0 <= y; }
int main() {
	fastio;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
			dp[i][j] = 987654321;
		}
	}
	dp[0][0] = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (isInside(i - 1, j)) {
				dp[i][j] = min(dp[i][j], dp[i-1][j] + max(0, arr[i][j] - arr[i-1][j] + 1));
			}
			if (isInside(i, j - 1)) {
				dp[i][j] = min(dp[i][j], dp[i][j-1] + max(0, arr[i][j] - arr[i][j-1] + 1));
			}
		}
	}
	cout << dp[n - 1][n - 1] << endl;
	return 0;
}