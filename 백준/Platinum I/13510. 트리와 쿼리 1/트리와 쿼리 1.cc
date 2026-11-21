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
int sz[MAX], depth[MAX], parent[MAX], top[MAX], in[MAX], out[MAX], cnt, visited[MAX], edge_no[MAX];
vector<int> graph[MAX];
vector<Data> inp[MAX];

struct SegTree {
	int tree[MAX * 4];
	void update(int v, int s, int e, int idx, int val) {
		if (idx < s || e < idx) return;
		if (s == e) {
			tree[v] = val;
			return;
		}
		int mid = (s + e) / 2;
		update(v * 2, s, mid, idx, val); update(v * 2 + 1, mid + 1, e, idx, val);
		tree[v] = max(tree[v * 2], tree[v * 2 + 1]);
	}
	int query(int v, int s, int e, int l, int r) {
		if (e < l || r < s) return 0;
		if (l <= s && e <= r) return tree[v];
		int mid = (s + e) / 2;
		return max(query(v * 2, s, mid, l, r), query(v * 2 + 1, mid + 1, e, l, r));
	}
} seg;

void update(int v, int w) {
	seg.update(1, 0, n - 1, in[v], w);
}
int query(int a, int b) {
	int ret = 0;
	while (top[a] != top[b]) {
		if (depth[top[a]] < depth[top[b]]) swap(a, b);
		int st = top[a];
		ret = max(ret, seg.query(1, 0, n - 1, in[st], in[a]));
		a = parent[st];
	}
	if (depth[a] > depth[b]) swap(a, b);
	if (depth[a] != depth[b])
		ret = max(ret, seg.query(1, 0, n - 1, in[a] + 1, in[b]));
	return ret;
}
void dfs(int v) {
	visited[v] = 1;
	for (Data d : inp[v]) {
		int i = d.node, w = d.weight, no = d.no;
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
	in[v] = cnt++;
	for (auto& i : graph[v]) {
		top[i] = ((i == graph[v][0]) ? top[v] : i);
		dfs2(i);
	}
	out[v] = cnt;
}
int main() {
	fastio;
	memset(seg.tree, 0, sizeof(seg.tree));
	cin >> n;
	for (int i = 0; i < n - 1; ++i) {
		int a, b, c;
		cin >> a >> b >> c;
		inp[a].push_back({ b, c, i });
		inp[b].push_back({ a, c, i });
	}
	dfs(1); dfs1(1); dfs2(1);
	for (int i = 1; i <= n; ++i) {
		for (auto& j : inp[i]) {
			if (parent[j.node] == i) edge_no[j.no] = j.node;
			else edge_no[j.no] = i;
			update(edge_no[j.no], j.weight);
		}
	}
	cin >> q;
	while (q--) {
		int op, a, b;
		cin >> op >> a >> b;
		if (op == 1) update(edge_no[a - 1], b);
		else cout << query(a, b) << endl;
	}
	return 0;
}