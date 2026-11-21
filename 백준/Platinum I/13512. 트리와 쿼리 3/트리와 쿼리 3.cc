#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

struct Data {
	int node, weight, no;
};

const int MAX = 100127;
int n, q;
int sz[MAX], depth[MAX], parent[MAX], top[MAX], in[MAX], in_r[MAX], cnt, visited[MAX];
vector<int> graph[MAX], inp[MAX];

struct SegTree {
	int tree[MAX * 4];
	void update(int v, int s, int e, int idx) {
		if (idx < s || e < idx) return;
		if (s == e) {
			tree[v] ^= 1;
			return;
		}
		int mid = (s + e) / 2;
		update(v * 2, s, mid, idx); update(v * 2 + 1, mid + 1, e, idx);
		tree[v] = tree[v * 2] + tree[v * 2 + 1];
	}
	int query(int v, int s, int e, int l, int r) {
		if (e < l || r < s) return 0;
		if (l <= s && e <= r) return tree[v];
		int mid = (s + e) / 2;
		return query(v * 2, s, mid, l, r) + query(v * 2 + 1, mid + 1, e, l, r);
	}
} seg;

void update(int v) {
	seg.update(1, 0, n - 1, in[v]);
}
int query(int v) {
	pair<int, int> last_black = { -1, -1 };
	while (top[v] != 0) {
		int val = seg.query(1, 0, n - 1, in[top[v]], in[v]);
		if (val) last_black = { top[v], v };
		v = parent[top[v]];
	}
	int val = seg.query(1, 0, n - 1, 0, in[v]);
	if (val) last_black = { 1, v };

	if (last_black == make_pair(-1, -1)) return -1;
	int lo = in[last_black.first], hi = in[last_black.second];
	while (lo < hi) {
		int mid = (lo + hi) / 2;
		if (seg.query(1, 0, n - 1, lo, mid)) hi = mid;
		else lo = mid + 1;
	}
	return in_r[lo];
}
void dfs(int v) {
	visited[v] = 1;
	for (auto& i : inp[v]) {
		if (!visited[i]) {
			graph[v].push_back(i);
			dfs(i);
		}
	}
}
void dfs1(int v) {
	sz[v] = 1;
	for (auto& i : graph[v]) {
		depth[i] = depth[v] + 1;
		parent[i] = v;
		dfs1(i);
		sz[v] += sz[i];
		if (sz[i] > sz[graph[v][0]]) swap(i, graph[v][0]);
	}
}
void dfs2(int v) {
	in[v] = cnt;
	in_r[cnt++] = v;
	for (auto& i : graph[v]) {
		top[i] = ((i == graph[v][0]) ? top[v] : i);
		dfs2(i);
	}
}
int main() {
	fastio;
	memset(seg.tree, 0, sizeof(seg.tree));
	cin >> n;
	for (int i = 0; i < n - 1; ++i) {
		int a, b;
		cin >> a >> b;
		inp[a].push_back(b);
		inp[b].push_back(a);
	}
	dfs(1); dfs1(1); dfs2(1);
	cin >> q;
	while (q--) {
		int op, v;
		cin >> op >> v;
		if (op == 1) update(v);
		else cout << query(v) << endl;
	}
	return 0;
}