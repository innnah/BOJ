#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<vector<int>> graph;
vector<ll> visited;
ll ret = 0;

ll f(ll n) { return n * (n - 1) / 2; }

ll dfs(int v) {
    visited[v] = 1;
    for (int i : graph[v]) {
        if (!visited[i]) {
            visited[v] += dfs(i);
        }
    }
    ret += f(n) - f(n - visited[v]);
    return visited[v];
}

int main() {
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    cin >> n;
    graph.assign(n + 1, vector<int>());
    visited.assign(n + 1, 0);
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(1);
    cout << ret - f(n) << '\n';
    return 0;
}