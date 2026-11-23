#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
using namespace std;

struct info {
    ll cur_dist, node, eaten;
};
struct comp {
    bool operator()(info a, info b) {
        return (a.cur_dist > b.cur_dist);
    }
};

ll dist[2][100005];
vector<vector<int>> graph[100005];
ll INF = 2 * pow(10, 9) + 5;
int v, e;
void dijkstra(int start) {
    priority_queue<info, vector<info>, comp> q;
    q.push({ 0, start, 0 });
    dist[0][start] = 0;
    while (!q.empty()) {
        ll cur_dist = q.top().cur_dist, node = q.top().node, eaten = q.top().eaten;
        q.pop();
        if (dist[eaten][node] < cur_dist) continue;
        for (int i = 0; i < graph[node].size(); ++i) {
            vector<int> ne = graph[node][i];
            ll cost = dist[eaten][node] + ne[1];
            if (cost < dist[eaten][ne[0]]) {
                dist[eaten][ne[0]] = cost;
                q.push({ cost, ne[0], eaten });
            }
            if (!eaten) {
                cost -= ne[2];
                if (cost < dist[1][ne[0]]) {
                    dist[1][ne[0]] = cost;
                    q.push({ cost, ne[0], 1 });
                }
            }
        }
    }
}
int main() {
    scanf("%d %d", &v, &e);
    fill(dist[0], dist[2], INF);
    for (int i = 0; i < e; ++i) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        graph[a].push_back({ b,c,d });
        graph[b].push_back({ a,c,d });
    }
    dijkstra(1);
    for (int i = 2; i <= v; ++i) {
        printf("%lld\n", min(dist[0][i], dist[1][i]));
    }
    return 0;
}