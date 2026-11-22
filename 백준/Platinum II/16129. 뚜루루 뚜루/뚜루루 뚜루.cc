#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, r, c, dx[4] = { 0, 0, -1, 1 }, dy[4] = { -1, 1, 0, 0 }, board[10][12117], visited[10][12117];
vector<int> seq = { 1, 0, 0, 1, 0 };
inline bool isInside(int x, int y) { return 0 <= x && x < r && 0 <= y && y < c; }
ll search(int x, int y, int dep) {
	if (dep == 5) {
		return 1;
	}
	ll ret = 0;
	for (int i = 0; i < 4; ++i) {
		int nx = x + dx[i], ny = y + dy[i];
		if (isInside(nx, ny) && !visited[nx][ny] && board[nx][ny] == seq[dep]) {
			visited[nx][ny] = 1;
			ret += search(nx, ny, dep + 1);
			visited[nx][ny] = 0;
		}
	}
	return ret;
}
ll count(int row, int column) {
	ll ret = 0;
	r = row, c = column;
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			if (board[i][j]) {
				visited[i][j] = 1;
				ret += search(i, j, 1);
				visited[i][j] = 0;
			}
		}
	}
	return ret;
}
int main() {
	fastio;
	cin >> n >> m;
	int d = 0;
	for (int i = 0; i < 10; ++i) {
		for (int j = 0; j < m; ++j) {
			board[i][j] = seq[d];
			d = (d + 1) % 5;
		}
	}

	ll cnt1 = count(5, m);
	ll cnt2 = count(n % 5, m);
	ll cnt3 = count(10, m) - cnt1 * 2;
	ll cnt4 = count(5 + n % 5, m) - (cnt1 + cnt2);

	ll ret = cnt1 * (ll)(n / 5) + cnt2;
	if (n / 5) ret += cnt3 * (ll)(n / 5 - 1) + cnt4;
	cout << ret;
	return 0;
}