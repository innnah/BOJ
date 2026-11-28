#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAX = 200127;
int n, q, arr[MAX], tree[1 << 19];
map<int, int> p;
int query(int v, int s, int e, int l, int r, int val) {
	if (e < l || r < s) return 0;
	if (l <= s && e <= r) {
		int sz = e - s + 1;
		int expo = p[sz];
		//cout << v << " " << (1 << (18 - expo)) << " " << ((s ^ val) >> expo) << endl;
		return tree[(1 << (18 - expo)) + ((s ^ val) >> expo)];
	}
	int mid = (s + e) / 2;
	return query(v * 2, s, mid, l, r, val) ^ query(v * 2 + 1, mid + 1, e, l, r, val);
}
int update(int v, int s, int e, int idx, int val) {
	if (idx < s || e < idx) return tree[v];
	if (s == e) {
		return tree[v] ^= val;
	}
	int mid = (s + e) / 2;
	return tree[v] = update(v * 2, s, mid, idx, val) ^ update(v * 2 + 1, mid + 1, e, idx, val);
}
int main() {
	fastio;
	for (int i = 0; i < 20; ++i) {
		p[1 << i] = i;
	}
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
		update(1, 0, 262143, i, arr[i]);
	}
	cin >> q;
	while (q--) {
		int op;
		cin >> op;
		if (op == 1) {
			int a, b, c;
			cin >> a >> b >> c;
			if (c < 262144)
				cout << query(1, 0, 262143, a, b, c) << endl;
			else
				cout << 0 << endl;
		}
		else {
			int a, b;
			cin >> a >> b;
			update(1, 0, 262143, a, b);
		}
	}
	return 0;
}