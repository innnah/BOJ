#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;
int n, m;
vector<vector<pair<int, int>>> graph;
vector<int> distance_, trace_;
pair<int, int> closed_;

void dijkstra(int start) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
    q.push({0, start});
    distance_[start] = 0;
    while (!q.empty()) {
        auto [dist, node] = q.top(); q.pop();
        if (distance_[node] < dist) continue;
        for (auto& ne : graph[node]) {
            if (closed_ == make_pair(node, ne.first) || closed_ == make_pair(ne.first, node))
                continue;
            int cost = distance_[node] + ne.second;
            if (cost < distance_[ne.first]) {
                distance_[ne.first] = cost;
                trace_[ne.first] = node;
                q.push({cost, ne.first});
            }
        }
    }
}

vector<int> reconstruct(int v) {
    vector<int> path = {v};
    int tmp = trace_[v];
    while (tmp != 0) {
        path.push_back(tmp);
        tmp = trace_[tmp];
    }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    graph.assign(n + 1, vector<pair<int, int>>());
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }
    distance_.assign(n + 1, INF);
    trace_.assign(n + 1, 0);
    closed_ = {0, 0};
    dijkstra(1);
    vector<int> path = reconstruct(n);
    int original = distance_[n];
    int ret = 0;
    for (size_t i = 0; i + 1 < path.size(); i++) {
        closed_ = {path[i], path[i + 1]};
        distance_.assign(n + 1, INF);
        dijkstra(1);
        ret = max(distance_[n], ret);
    }
    if (ret == INF) cout << -1 << '\n';
    else cout << ret - original << '\n';
    return 0;
}