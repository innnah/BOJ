#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, seg[801270], lazy[801270], in[200127], out[200127], fruits[100127];
vector<int> tree[200127], querys[100127];
int cnt = -1;
void dfs(int v) {
	in[v] = ++cnt;
	for (auto& i : tree[v]) {
		dfs(i);
	}
	out[v] = cnt;
}
void lazy_update(int v, int s, int e) {
	if (lazy[v] != -1) {
		seg[v] = (e - s + 1) * lazy[v];
		if (s != e) {
			lazy[v * 2] = lazy[v];
			lazy[v * 2 + 1] = lazy[v];
		}
		lazy[v] = -1;
	}
}
int query(int v, int s, int e, int l, int r) {
	lazy_update(v, s, e);
	if (r < s || e < l) return 0;
	if (l <= s && e <= r) return seg[v];
	int mid = (s + e) / 2;
	return query(v * 2, s, mid, l, r) + query(v * 2 + 1, mid + 1, e, l, r);
}
int update(int v, int s, int e, int l, int r, int diff) {
	lazy_update(v, s, e);
	if (r < s || e < l) return seg[v];
	if (l <= s && e <= r) {
		lazy[v] = diff;
		lazy_update(v, s, e);
		return seg[v];
	}
	int mid = (s + e) / 2;
	return seg[v] = update(v * 2, s, mid, l, r, diff) + update(v * 2 + 1, mid + 1, e, l, r, diff);
}
int main() {
	fastio;
	memset(lazy, -1, sizeof(lazy));
	cin >> n >> m;
	int tmp;
	cin >> tmp;
	for (int i = 2; i <= n; ++i) {
		int a;
		cin >> a;
		tree[a].push_back(i);
	}
	for (int i = 1; i <= n; ++i) {
		cin >> fruits[i];
	}
	for (int i = 0; i < m; ++i) {
		int q;
		cin >> q;
		if (q == 1) {
			int a, b, c;
			cin >> a >> b >> c;
			querys[i] = { q, a, b, c };
			tree[a].push_back(b);
		}
		else {
			int a;
			cin >> a;
			querys[i] = { q, a };
		}
	}
	dfs(1);
	for (int i = 1; i <= n; ++i) {
		update(1, 0, n + m - 1, in[i], in[i], fruits[i]);
	}
	for (int i = 0; i < m; ++i) {
		vector<int> qu = querys[i];
		if (qu[0] == 1) {
			int a = qu[1], b = qu[2], c = qu[3];
			update(1, 0, n + m - 1, in[b], in[b], c);
		}
		else {
			int a = qu[1];
			int ret = query(1, 0, n + m - 1, in[a], out[a]);
			if (ret) cout << ret << endl;
			else cout << -1 << endl;
		}
	}
	return 0;
}