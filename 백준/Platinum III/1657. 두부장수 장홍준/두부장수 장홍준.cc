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

map<pair<char, char>, int> price = { {{'A', 'A'}, 10}, { {'A', 'B'}, 8}, { {'A', 'C'}, 7}, { {'A', 'D'}, 5}, { {'A', 'F'}, 1}, { {'B', 'A'}, 8}, 
	{ {'B', 'B'}, 6}, { {'B', 'C'}, 4}, { {'B', 'D'}, 3}, { {'B', 'F'}, 1}, { {'C', 'A'}, 7}, { {'C', 'B'}, 4}, { {'C', 'C'}, 3}, { {'C', 'D'}, 2}, 
	{ {'C', 'F'}, 1}, { {'D', 'A'}, 5}, { {'D', 'B'}, 3}, { {'D', 'C'}, 2}, { {'D', 'D'}, 2}, { {'D', 'F'}, 1}, { {'F', 'A'}, 1}, { {'F', 'B'}, 1}, 
	{ {'F', 'C'}, 1}, { {'F', 'D'}, 1}, { {'F', 'F'}, 0} };
int n, m, dp[15][15][1<<14];
string tofu[14];
int dpf(int r, int c, int sel) {
	if (c == m) return dpf(r + 1, 0, sel);
	if (r == n) return 0;
	int& ret = dp[r][c][sel];
	if (ret != -1) return ret;
	if (sel % 2) return dpf(r, c + 1, (sel-1)/2);
	ret = max(ret, dpf(r, c + 1, sel / 2));
	if (c < m - 1 && !(sel & (1<<1))) ret = max(ret, dpf(r, c + 2, sel / 4) + price[{tofu[r][c], tofu[r][c + 1]}]);
	if (r < n - 1) ret = max(ret, dpf(r, c + 1, sel / 2 + (1 << (m-1))) + price[{tofu[r][c], tofu[r + 1][c]}]);
	return ret;
}
int main() {
	fastio;
	cin >> n >> m;
	for (int i = 0; i < n; ++i) {
		cin >> tofu[i];
	}
	memset(dp, -1, sizeof(dp));
	cout << dpf(0, 0, 0);
	return 0;
}