#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

struct Node {
	ll ans, mx, mn;
};

int n, q;
ll arr[100127];
Node tree[400127];

inline Node merge(const Node& a, const Node& b) {
	return { max(max(a.ans, b.ans), b.mx - a.mn), max(a.mx, b.mx), min(a.mn, b.mn) };
}
void init(int v, int s, int e) {
	if (s == e) {
		tree[v] = { 0, arr[s], arr[s] };
		return;
	}
	int mid = s + e >> 1;
	init(v * 2, s, mid); init(v * 2 + 1, mid + 1, e);
	tree[v] = merge(tree[v * 2], tree[v * 2 + 1]);
}
Node query(int v, int s, int e, int l, int r) {
	if (e < l || r < s) return { -127, -1234567890, 1234567890 };
	if (l <= s && e <= r) return tree[v];
	int mid = s + e >> 1;
	return merge(query(v * 2, s, mid, l, r), query(v * 2 + 1, mid + 1, e, l, r));
}
void update(int v, int s, int e, int idx, ll val) {
	if (idx < s || e < idx) return;
	if (s == e) {
		tree[v] = { 0, val, val };
		return;
	}
	int mid = s + e >> 1;
	update(v * 2, s, mid, idx, val); update(v * 2 + 1, mid + 1, e, idx, val);
	tree[v] = merge(tree[v * 2], tree[v * 2 + 1]);
}

int main() {
	fastio;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	init(1, 0, n - 1);
	cin >> q;
	while (q--) {
		int op;
		cin >> op;
		if (op == 2) {
			int l, r;
			cin >> l >> r;
			cout << query(1, 0, n - 1, l - 1, r - 1).ans << endl;
		}
		else {
			ll k, x;
			cin >> k >> x;
			update(1, 0, n - 1, k - 1, x);
		}
	}
	return 0;
}