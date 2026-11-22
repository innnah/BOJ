#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

ll n, dp[201][201];
string st;
inline int getCnt(int s, int e) {
	if (st[s] == '?' && st[e] == '?') {
		return 3;
	}
	else if (st[s] == '?') {
		if (st[e] == ')' || st[e] == '}' || st[e] == ']') return 1;
	}
	else if (st[e] == '?') {
		if (st[s] == '(' || st[s] == '{' || st[s] == '[') return 1;
	}
	else if (st[s] == '(' && st[e] == ')') return 1;
	else if (st[s] == '{' && st[e] == '}') return 1;
	else if (st[s] == '[' && st[e] == ']') return 1;
	return 0;
}
ll dpf(int s, int e) {
	if (s > e) return 1;
	ll& ret = dp[s][e];
	if (ret != -1) return ret;
	ll over = 0;
	ret = getCnt(s, e) * dpf(s + 1, e - 1);
	if (ret >= 100000) over = 1;
	ret %= 100000;
	for (int i = s + 1; i <= e - 2; i += 2) {
		ret += getCnt(s, i) * dpf(s + 1, i - 1) * dpf(i + 1, e);
		if (ret >= 100000) over = 1;
		ret %= 100000;
	}
	ret += over * 100000;
	return ret;
}
int main() {
	fastio;
	cin >> n;
	cin >> st;
	if (n % 2 == 1) {
		cout << 0;
		return 0;
	}
	memset(dp, -1, sizeof(dp));
	ll ret = dpf(0, n - 1);
	if (ret >= 100000) {
		cout << to_string(ret).substr(1, 5);
	}
	else cout << ret;
	return 0;
}