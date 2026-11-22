#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>
#include <random>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt
#define pll pair<ll, ll>
#define pint pair<int, int>

int n, m, dp[15][15][1<<14];
int dpf(int r, int c, int sel) {
	if (c == m) return dpf(r + 1, 0, sel);
	if (r == n) return 1;
	int& ret = dp[r][c][sel];
	if (ret != -1) return ret;
	if (sel % 2) return dpf(r, c + 1, (sel-1)/2);
	ret = 0;
	if (c < m - 1 && !(sel & (1<<1))) ret = (ret + dpf(r, c + 2, sel / 4)) % 9901;
	if (r < n - 1) ret = (ret + dpf(r, c + 1, sel / 2 + (1 << (m-1)))) % 9901;
	return ret;
}
int main() {
	fastio;
	cin >> n >> m;
	memset(dp, -1, sizeof(dp));
	cout << dpf(0, 0, 0);
	return 0;
}