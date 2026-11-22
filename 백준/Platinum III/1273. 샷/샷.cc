#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, arr[4][300127], ans[300127], querys[300127], tree[5301270];
ll ds[3] = { 1, 3, -5 };
pii shoot[300127];
int init(int v, int s, int e) {
	if (s == e) return tree[v] = 1;
	int mid = (s + e) / 2;
	return tree[v] = init(v * 2, s, mid) + init(v * 2 + 1, mid + 1, e);
}
int update(int v, int s, int e, int idx, int val) {
	if (idx < s or idx > e) return tree[v];
	if (s == e) return tree[v] = val;
	int mid = (s + e) / 2;
	return tree[v] = update(v * 2, s, mid, idx, val) + update(v * 2 + 1, mid + 1, e, idx, val);
}
int query(int v, int s, int e, int val) {
	if (s == e) return s;
	int mid = (s + e) / 2;
	if (tree[v * 2] < val) return query(v * 2 + 1, mid + 1, e, val - tree[v * 2]);
	return query(v * 2, s, mid, val);
}
int main() {
	fastio;
	cin >> n;
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> arr[i][j];
		}
	}
	for (int i = 0; i < n; ++i) {
		arr[3][i] = 987654321;
	}
	for (int i = 1; i < 4; ++i) {
		for (int j = 0; j < n; ++j) {
			arr[i][j] += arr[i - 1][j];
		}
	}
	init(1, 1, 1300127);
	cin >> m;
	for (int i = 0; i < m; ++i) {
		cin >> querys[i];
		shoot[i] = { query(1, 1, 1300127, querys[i]), i };
		update(1, 1, 1300127, shoot[i].first, 0);
	}
	sort(shoot, shoot + m);
	priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
	for (int i = 0; i < n; ++i) {
	    pq.push({ arr[0][i], i, 0 });
	}
	ll score = n;
	for (int i = 0; i < m; ++i) {
		int s = shoot[i].first;
		vector<int> v = pq.top();
		while (v[0] < s) {
			//cout << v[0] << endl;
			pq.pop();
			score += ds[v[2]];
			pq.push({ arr[v[2] + 1][v[1]], v[1], v[2] + 1 });
			v = pq.top();
		}
		ans[shoot[i].second] = score;
	}
	for (int i = 0; i < m; ++i) {
		cout << ans[i] << endl;
	}
	return 0;
}