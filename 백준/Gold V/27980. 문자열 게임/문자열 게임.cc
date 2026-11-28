#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, dp[5127][5127];
string s, t;
int dpf(int idx, int wh) {
	if (idx == m) return 0;
	if (wh < 0 || wh >= n) return 0;
	int& ret = dp[idx][wh];
	if (ret != -1) return ret;
	ret = 0;
	if (s[wh] == t[idx]) ret += 1;
	ret += max(dpf(idx + 1, wh - 1), dpf(idx + 1, wh + 1));
	return ret;
}
int main() {
	fastio;
	cin >> n >> m;
	cin >> s >> t;
	memset(dp, -1, sizeof(dp));
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		ret = max(ret, dpf(0, i));
	}
	cout << ret;
	return 0;
}