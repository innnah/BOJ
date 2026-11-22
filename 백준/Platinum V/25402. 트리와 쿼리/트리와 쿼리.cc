#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAXN = 250005;
vector<int> graph[MAXN];
int n, m, parent[MAXN], unionfind[MAXN];
long long len[MAXN];
bool visited[MAXN];
void getParent(int v) {
	visited[v] = 1;
	for (auto& i : graph[v]) {
		if (!visited[i]) {
			parent[i] = v;
			getParent(i);
		}
	}
}
int find(int v) {
	if (v != unionfind[v]) return unionfind[v] = find(unionfind[v]);
	return v;
}
void merge(int u, int v) {
	u = find(u);
	v = find(v);
	if (u != v) {
		unionfind[v] = unionfind[u];
		len[u] += len[v];
	}
}
int main() {
	fastio;
	cin >> n;
	for (int i = 0; i < n - 1; ++i) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}
	getParent(1);
	cin >> m;
	while (m--) {
		int k;
		cin >> k;
		vector<bool> isinS(n+1);
		vector<int> s(k);
		for (int i = 0; i < k; ++i) {
			cin >> s[i];
			isinS[s[i]] = 1;
			len[s[i]] = 1;
			unionfind[s[i]] = s[i];
		}
		for (int i = 0; i < k; ++i) {
			if (isinS[parent[s[i]]]) {
				merge(parent[s[i]], s[i]);
			}
		}
		long long ret = 0;
		for (int i = 0; i < k; ++i) {
			if (find(s[i]) == s[i]) ret += len[s[i]] * (len[s[i]] - 1) / 2;
		}
		cout << ret << endl;
	}
	return 0;
}