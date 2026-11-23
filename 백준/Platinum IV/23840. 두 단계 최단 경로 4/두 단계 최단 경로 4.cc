#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

typedef ll cache_type;
const int MAX = 22;
const int MAXN = 100005;
const ll INF = 9876543212345678;
int n, m, x, z, k;
cache_type cache[MAX][1 << MAX];
vector<pair<ll, ll>> graph[MAXN];
int p[MAX];
ll dist[MAXN];
ll c[MAX][MAX];
void dijkstra(int start) {
    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> q;
    q.push({ 0, start });
    dist[start] = 0;
    while (!q.empty()) {
        pair<ll, ll> poped = q.top();
        q.pop();
        ll cur_dist = poped.first, node = poped.second;
        if (dist[node] < cur_dist) continue;
        for (int i = 0; i < graph[node].size(); ++i) {
            pair<ll, ll> ne = graph[node][i];
            ll cost = dist[node] + ne.second;
            if (cost < dist[ne.first]) {
                dist[ne.first] = cost;
                q.push({ cost, ne.first });
            }
        }
    }
}
cache_type dp(int here, int visited) {
    if (visited == (1 << (k+1)) - 1) return c[here][k+1];
    cache_type& ret = cache[here][visited];
    if (ret >= 0) return ret;
    ret = INF;
    for (int i = 1; i < k+1; ++i) {
        if (visited & (1 << i)) continue;
        ret = min(ret, c[here][i] + dp(i, visited | (1 << i)));
    }
    return ret;
}
int main() {
    fastio;
    memset(cache, -1, sizeof(cache));
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; ++i) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        graph[a].push_back({ b, c });
        graph[b].push_back({ a, c });
    }
    scanf("%d %d", &x, &z);
    scanf("%d", &k);
    for (int i = 0; i < k; ++i) {
        scanf("%d", &p[i+1]);
    }
    p[0] = x;
    p[k+1] = z;
    for (int i = 0; i < k+2; ++i) {
        fill(dist, dist+n+1, INF);
        dijkstra(p[i]);
        for (int j = 0; j < k + 2; ++j) {
            c[i][j] = dist[p[j]];
        }
    }
    ll ret = dp(0, 1);
    if (ret == INF) printf("-1");
    else printf("%lld", ret);
    return 0;
}