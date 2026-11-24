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

map<pair<char, char>, int> price = { {{'A', 'A'}, 100}, { {'A', 'B'}, 70}, { {'A', 'C'}, 40}, { {'A', 'F'}, 0}, 
    { {'B', 'A'}, 70}, { {'B', 'B'}, 50}, { {'B', 'C'}, 30}, { {'B', 'F'}, 0}, 
    { {'C', 'A'}, 40}, { {'C', 'B'}, 30}, { {'C', 'C'}, 20}, { {'C', 'F'}, 0}, 
    { {'F', 'A'}, 0}, { {'F', 'B'}, 0}, { {'F', 'C'}, 0}, { {'F', 'F'}, 0} };
int n, m, dp[12][12][1<<11];
string tofu[11];
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
	cin >> n;
    m = n;
	for (int i = 0; i < n; ++i) {
		cin >> tofu[i];
	}
	memset(dp, -1, sizeof(dp));
	cout << dpf(0, 0, 0);
	return 0;
}