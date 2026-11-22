#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, price[1000127], visited[1000127], mxval[1000127], ans[1000127];
vector<int> tree[1000127];
void dfs(int v, int s) {
	visited[v] = 1;
	int s2 = 0;
	pii mx = { -1, -1 };
	for (auto& i : tree[v]) {
		if (!visited[i]) {
			s2 += mxval[i];
			if (mx.first < mxval[i]) {
				mx.second = mx.first;
				mx.first = mxval[i];
			}
			else if (mx.second < mxval[i]) mx.second = mxval[i];
		}
	}
	ans[v] = s + s2;
	for (auto& i : tree[v]) {
		if (!visited[i]) {
			int ns = max(s, price[v]);
			if (mxval[i] == mx.first) ns = max(ns, mx.second);
			else ns = max(ns, mx.first);
			dfs(i, ns);
		}
	}
}
void dfs2(int v) {
	visited[v] = 1;
	mxval[v] = price[v];
	for (auto& i : tree[v]) {
		if (!visited[i]) {
			dfs2(i);
			mxval[v] = max(mxval[v], mxval[i]);
		}
	}
}
int main() {
	fastio;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cin >> price[i];
	}
	for (int i = 0; i < n - 1; ++i) {
		int a, b;
		cin >> a >> b;
		tree[a].push_back(b);
		tree[b].push_back(a);
	}
	dfs2(1);
	memset(visited, 0, sizeof(visited));
	dfs(1, 0);
	int ret = 0;
	for (int i = 1; i <= n; ++i) {
		ret = max(ret, ans[i]);
	}
	cout << ret;
	return 0;
}