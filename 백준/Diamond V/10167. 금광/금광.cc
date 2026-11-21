#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

const int MAX = 3127;
const ll INF = 98765432123456;

struct Data {
	ll x, y, p, i;
};
struct Node {
	ll sum, lans, rans, ans;
};
int n;
Data arr[MAX];
Node tree[MAX * 4];
inline Node merge(const Node& a, const Node& b) {
	return { a.sum + b.sum, max(a.lans, a.sum + b.lans), max(b.rans, a.rans + b.sum), max(a.rans + b.lans, max(a.ans, b.ans)) };
}
Node update(int v, int s, int e, int idx, ll val) {
	if (idx < s || e < idx) return tree[v];
	if (s == e) {
		if (tree[v].ans == -INF) {
			tree[v].sum = tree[v].lans = tree[v].rans = tree[v].ans = 0;
		}
		tree[v].sum += val; tree[v].lans += val; tree[v].rans += val; tree[v].ans += val;
		return tree[v];
	}
	int mid = s + e >> 1;
	Node le = update(v << 1, s, mid, idx, val), ri = update(v << 1 | 1, mid + 1, e, idx, val);
	return tree[v] = merge(le, ri);
}
Node query(int v, int s, int e, int l, int r) {
	if (r < s || e < l) return { 0, -INF, -INF, -INF };
	if (l <= s && e <= r) return tree[v];
	int mid = s + e >> 1;
	Node le = query(v << 1, s, mid, l, r), ri = query(v << 1 | 1, mid + 1, e, l, r);
	return merge(le, ri);
}
int main() {
	fastio;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		ll a, b, c;
		cin >> a >> b >> c;
		arr[i].x = a; arr[i].y = b; arr[i].p = c, arr[i].i = i;
	}
	sort(arr, arr + n, [](const Data& a, const Data& b) { return a.x < b.x; });
	int cnt = 0;
	arr[0].i = 0;
	for (int i = 1; i < n; ++i) {
		if (arr[i - 1].x != arr[i].x) ++cnt;
		arr[i].i = cnt;
	}
	sort(arr, arr + n, [](const Data& a, const Data& b) { return a.y < b.y; });

	ll ret = 0;
	int i = 0;
	while (i < n) {
		for (int j = 0; j < n * 4 + 10; ++j) {
			tree[j] = { 0, -INF, -INF, -INF };
		}
		int j = i;
		while (j < n) {
			int yval = arr[j].y;
			while (arr[j].y == yval) {
				update(1, 0, n - 1, arr[j].i, arr[j].p); ++j;
			}
			Node qry_ans = query(1, 0, n - 1, 0, n - 1);
			ret = max(ret, qry_ans.ans);
		}
		int yval1 = arr[i].y;
		while (arr[i].y == yval1) {
			++i;
		}
	}
	cout << ret;
	return 0;
}