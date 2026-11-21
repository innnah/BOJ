#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, arr[500127], last_idx[500127], tree[2001270], lazy[2001270];
void lazy_update(int v, int s, int e) {
	if (lazy[v]) {
		tree[v] += lazy[v];
		if (s != e) {
			lazy[v * 2] += lazy[v];
			lazy[v * 2 + 1] += lazy[v];
		}
		lazy[v] = 0;
	}
}
int query(int v, int s, int e, int l, int r) {
	lazy_update(v, s, e);
	if (e < l || r < s) return -1;
	if (l <= s && e <= r) return tree[v];
	int mid = s + e >> 1;
	return max(query(v * 2, s, mid, l, r), query(v * 2 + 1, mid + 1, e, l, r));
}
void update(int v, int s, int e, int l, int r, int val) {
	lazy_update(v, s, e);
	if (e < l || r < s) return;
	if (l <= s && e <= r) {
		lazy[v] += val;
		lazy_update(v, s, e);
		return;
	}
	int mid = s + e >> 1;
	update(v * 2, s, mid, l, r, val); update(v * 2 + 1, mid + 1, e, l, r, val);
	tree[v] = max(tree[v * 2], tree[v * 2 + 1]);
}
int main() {
	fastio;
	cin >> n >> m;
	for (int i = 1; i <= n; ++i) {
		cin >> arr[i];
	}
	int hm = (m + 1) / 2;
	memset(last_idx, -1, sizeof(last_idx));
	for (int i = 1; i <= n; ++i) {
		if (arr[i]) {
			update(1, 0, n, last_idx[arr[i]] + 1, i - 1, 1);
			last_idx[arr[i]] = i - 1;
		}
		if (i >= hm) {
			int q_val = query(1, 0, n, 0, i - hm);
			update(1, 0, n, i, i, q_val);
		}
	}
	lazy_update(1, 0, n);
	cout << tree[1];
	return 0;
}