#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

ll n, m, ans, parent[100127], cost[100127], lship[100127], sum[100127];
priority_queue<ll> pq[100127];
vector<int> graph[100127];
void dfs(int v) {
	pq[v].push(cost[v]);
	sum[v] = cost[v];
	for (auto& i : graph[v]) {
		dfs(i);
		if (pq[i].size() > pq[v].size()) {
			pq[v].swap(pq[i]);
			sum[v] = sum[i];
		}
	}
	for (auto& i : graph[v]) {
		while (!pq[i].empty()) {
			pq[v].push(pq[i].top());
			sum[v] += pq[i].top();
			pq[i].pop();
		}
	}
	while (sum[v] > m) {
		sum[v] -= pq[v].top();
		pq[v].pop();
	}
	ans = max(ans, (ll)pq[v].size() * lship[v]);
}
int main() {
	fastio;
	cin >> n >> m;
	for (int i = 1; i <= n; ++i) {
		cin >> parent[i] >> cost[i] >> lship[i];
		graph[parent[i]].push_back(i);
	}
	dfs(1);
	cout << ans << endl;
	return 0;
}