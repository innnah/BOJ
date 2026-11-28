#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

struct Query {
	int s, e, idx;
	bool operator< (const Query& x) {
		return vector<int>{s, e, idx} < vector<int>{x.s, x.e, x.idx};
	}
};

const int MAXN = 1001270;
int n, q, ans[100127], tree[MAXN*4+10];
string s;
int query(int v, int s, int e, int l, int r) {
	if (e < l || r < s) return 0;
	if (l <= s && e <= r) return tree[v];
	int mid = s + e >> 1;
	return query(v * 2, s, mid, l, r) + query(v * 2 + 1, mid + 1, e, l, r);
}
int update(int v, int s, int e, int idx, int val) {
	if (idx < s || e < idx) return tree[v];
	if (s == e) {
		tree[v] = val;
		return tree[v];
	}
	int mid = s + e >> 1;
	return tree[v] = update(v * 2, s, mid, idx, val) + update(v * 2 + 1, mid + 1, e, idx, val);
}
int main() {
	fastio;
	cin >> s;
	n = s.length();
	vector<int> stack;
	vector<pair<int, int>> braces;
	for (int i = 0; i < n; ++i) {
		if (s[i] == '(') {
			stack.push_back(i);
		}
		else {
			if (!stack.empty()) {
				braces.push_back({ stack.back(), i });
				stack.pop_back();
			}
		}
	}

	sort(braces.begin(), braces.end());

	vector<Query> querys;
	cin >> q;
	for (int i = 0; i < q; ++i) {
		int a, b;
		cin >> a >> b;
		a -= 1;
		b -= 1;
		querys.push_back({ a, b, i });
	}

	sort(querys.begin(), querys.end());

	int idx = braces.size() - 1;
	for (int i = q - 1; i >= 0; --i) {
		//cout << i << " " << idx << " " << querys[i].s << " " << querys[i].e << endl;
		while (idx >= 0 && braces[idx].first >= querys[i].s) {
			update(1, 0, n - 1, braces[idx].second, 1);
			idx -= 1;
		}
		ans[querys[i].idx] = query(1, 0, n - 1, 0, querys[i].e) * 2;
	}
	for (int i = 0; i < q; ++i) {
		cout << ans[i] << endl;
	}
	return 0;
}