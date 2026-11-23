#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

struct Edge {
	int a, b, w;
};

struct State {
	int v, w, d;
};

int n, m;
Edge edges[100127];
unordered_map<int, vector<int>> tree[50127];
unordered_map<int, int> visited[50127];
int main() {
	fastio;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> edges[i].a >> edges[i].b >> edges[i].w;
		tree[edges[i].a][edges[i].w].push_back(edges[i].b);
		tree[edges[i].b][edges[i].w].push_back(edges[i].a);
	}
	queue<State> q;
	for (auto& ne : tree[1]) {
		for (auto& v : ne.second) {
			q.push({v, ne.first, 1});
			visited[v][ne.first] = 1;
		}
	}
	while (!q.empty()) {
		State s = q.front(); q.pop();
		int nw = s.w + 1;
		for (auto& nv : tree[s.v][nw]) {
			if (visited[nv].find(nw) == visited[nv].end()) {
				q.push({nv, nw, s.d + 1});
				visited[nv][nw] = s.d + 1;
			}
		}
		nw = s.w - 1;
		for (auto& nv : tree[s.v][nw]) {
			if (visited[nv].find(nw) == visited[nv].end()) {
				q.push({nv, nw, s.d + 1});
				visited[nv][nw] = s.d + 1;
			}
		}
	}
	for (int i = 1; i <= n; ++i) {
		int ans = 987654321;
		for (auto& ne : visited[i]) {
			ans = min(ans, ne.second);
		}
		if (ans == 987654321) cout << -1 << " ";
		else cout << ans << " ";
	}
	return 0;
}