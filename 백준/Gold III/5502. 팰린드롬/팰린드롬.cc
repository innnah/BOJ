#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, dp[5127][5127];
string s;
int dpf(int a, int b) {
	if (a >= b) return 0;
	int& ret = dp[a][b];
	if (ret != -1) return ret;
	ret = 987654321;
	if (s[a] == s[b]) ret = min(ret, dpf(a + 1, b - 1));
	ret = min(ret, min(dpf(a + 1, b), dpf(a, b - 1)) + 1);
	return ret;
}
int main() {
	fastio;
	cin >> n >> s;
	memset(dp, -1, sizeof(dp));
	cout << dpf(0, n - 1);
	return 0;
}