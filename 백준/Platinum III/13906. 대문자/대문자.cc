#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

ll n, dp[1127];
string st;
const ll MOD = 1000000007;
ll dpf(int idx) {
	if (idx == n) return 1;
	ll& ret = dp[idx];
	if (ret != -1) return ret;
	ret = 1;
	vector<int> cnt(26, 0);
	for (int i = idx; i < n; ++i) {
		int ch = st[i] - 'a';
		++cnt[ch];
		if (cnt[ch] == 3) ret += dpf(i + 1);
		ret %= MOD;
	}
	return ret;
}
int main() {
	fastio;
	cin >> st;
	n = st.length();
	memset(dp, -1, sizeof(dp));
	ll ret = dpf(0);
	cout << (ret - 1 + MOD) % MOD;
	return 0;
}