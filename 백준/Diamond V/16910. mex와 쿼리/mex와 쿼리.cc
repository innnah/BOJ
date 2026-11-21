#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int> 

struct Query {
	ll q, l, r;
};

int n;
Query querys[100127];
int tree[801270];
int lazy1[801270], lazy2[801270];
vector<pair<ll, int>> nums;
void lazy_update(int v, int s, int e) {
	if (lazy1[v] != 2) {
		tree[v] = (e - s + 1) * lazy1[v];
		if (s != e) {
			lazy1[v * 2] = lazy1[v * 2 + 1] = lazy1[v];
			lazy2[v * 2] = lazy2[v * 2 + 1] = 0;
		}
		lazy1[v] = 2;
	}
	if (lazy2[v] != 0) {
		tree[v] = e - s + 1 - tree[v];
		if (s != e) {
			lazy2[v * 2] ^= 1;
			lazy2[v * 2 + 1] ^= 1;
		}
		lazy2[v] = 0;
	}
}
int update1(int v, int s, int e, int l, int r, int val) {
	lazy_update(v, s, e);
	if (e < l || r < s) return tree[v];
	if (l <= s && e <= r) {
		lazy1[v] = val;
		lazy2[v] = 0;
		lazy_update(v, s, e);
		return tree[v];
	}
	int mid = (s + e) / 2;
	return tree[v] = update1(v * 2, s, mid, l, r, val) + update1(v * 2 + 1, mid + 1, e, l, r, val);
}
int update2(int v, int s, int e, int l, int r) {
	lazy_update(v, s, e);
	if (e < l || r < s) return tree[v];
	if (l <= s && e <= r) {
		lazy2[v] ^= 1;
		lazy_update(v, s, e);
		return tree[v];
	}
	int mid = (s + e) / 2;
	return tree[v] = update2(v * 2, s, mid, l, r) + update2(v * 2 + 1, mid + 1, e, l, r);
}
ll mex(int v, int s, int e) {
    lazy_update(v, s, e);
	if (s == e) {
		return nums[s].first;
	}
	int mid = (s + e) / 2;
	lazy_update(v * 2, s, mid);
    lazy_update(v * 2 + 1, mid + 1, e);
	if (tree[v * 2] == mid - s + 1) {
		return mex(v * 2 + 1, mid + 1, e);
	}
	return mex(v * 2, s, mid);
}
int main() {
	fastio;
	cin >> n;
	vector<ll> tmp;
	for (int i = 0; i < n; ++i) {
		cin >> querys[i].q >> querys[i].l >> querys[i].r;
		tmp.push_back(querys[i].l);
		tmp.push_back(querys[i].r + 1);
	}
	tmp.push_back(1);
	sort(tmp.begin(), tmp.end());
	nums.push_back({ tmp[0], 0 });
	for (int i = 1; i < tmp.size(); ++i) {
		if (nums.rbegin()->first != tmp[i]) nums.push_back({ tmp[i], nums.size() });
	}
	for (int i = 0; i < 801270; ++i) {
		lazy1[i] = 2;
	}
	int t = nums.size();
	for (int i = 0; i < n; ++i) {
		int idx1 = lower_bound(nums.begin(), nums.end(), make_pair(querys[i].l, -1))->second;
		int idx2 = lower_bound(nums.begin(), nums.end(), make_pair(querys[i].r + 1, -1))->second - 1;
		if (querys[i].q == 1) {
			update1(1, 0, t - 1, idx1, idx2, 1);
		}
		else if (querys[i].q == 2) {
			update1(1, 0, t - 1, idx1, idx2, 0);
		}
		else {
			update2(1, 0, t - 1, idx1, idx2);
		}
		cout << mex(1, 0, t - 1) << endl;
	}
	return 0;
}