#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

ll dr[4] = { 0, 0, -1, 1 }, dc[4] = { -1, 1, 0, 0 }, n, m, v, arr[1127][1127], board[1127][1127], visited[1127][1127], cnt, grs[512712];
inline bool isInside(int r, int c) { return 0 <= r && r < n && 0 <= c && c < m; }
void dfs(int r, int c, int depth) {
	visited[r][c] = 1;
	grs[cnt] += arr[r][c] * ((depth % 2) * 2 - 1);
	for (int i = 0; i < 4; ++i) {
		int nr = r + dr[i], nc = c + dc[i];
		if (isInside(nr, nc) && !visited[nr][nc] && !board[nr][nc])
			dfs(nr, nc, depth+1);
	}
}
int main() {
	fastio;
	cin >> n >> m >> v;
	for (int i = 0; i < 2; ++i)
		for (int j = 0; j < n; ++j)
			for (int k = 0; k < m; ++k) {
				ll tmp;
				cin >> tmp;
				arr[j][k] += tmp * (1 - i * 2);
			}
	while (v--) {
		int r, c;
		cin >> r >> c;
		board[--r][--c] = 1;
		if (arr[r][c] != 0) {
			cout << "No"; return 0;
		}
	}
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) {
			if (!visited[i][j] && !board[i][j]) {
				dfs(i, j, 1); ++cnt;
			}
		}
	for (int i = 0; i < cnt; ++i) {
		if (grs[i]) {
			cout << "No"; return 0;
		}
	}
	cout << "Yes";
	return 0;
}