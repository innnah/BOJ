#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, point[1127];
ll dp[1127][1127][2], p[1127], psum[1127];
ll dpf(int a, int b, int x) {
	if (a == 0 && b == n-1) return 0;
	ll& ret = dp[a][b][x];
	if (ret != -1) return ret;
	ret = 98765432123456789LL;
	ll lsum = psum[n] - (psum[b + 1] - psum[a]);
	//cout << a << " " << b << " " << lsum << endl;
	if (a != 0) {
		ret = min(ret, dpf(a - 1, b, 0) + (ll)(point[x ? b : a] - point[a - 1]) * lsum);
	}
	if (b != n-1) {
		ret = min(ret, dpf(a, b + 1, 1) + (ll)(point[b + 1] - point[x ? b : a]) * lsum);
	}
	return ret;
}
int main() {
	fastio;
	cin >> n >> m;
	m -= 1;
	for (int i = 0; i < n; ++i) {
		cin >> point[i] >> p[i];
	}
	memset(dp, -1, sizeof(dp));
	for (int i = 0; i < n; ++i) {
		psum[i + 1] = psum[i] + p[i];
	}
	cout << dpf(m, m, 0);
	return 0;
}