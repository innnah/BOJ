#include <bits/stdc++.h>
#include <stdio.h>
using namespace std;
#define ll long long

const int MAX = 100005;
const int LOG = 20;
int n, m, c[MAX], d1[MAX];
ll d[MAX], parent[MAX][LOG];
vector<pair<int, ll>> graph[MAX];

void dfs(int v, ll depth, int depth1) {
    c[v] = 1;
    d[v] = depth;
    d1[v] = depth1;
    for (auto& i : graph[v]) {
        if (c[i.first]) continue;
        parent[i.first][0] = v;
        dfs(i.first, depth+i.second, depth1+1);
    }
}
void set_parent() {
    dfs(1, 0, 0);
    for (int i = 1; i < LOG; ++i) {
        for (int j = 1; j <= n; ++j) {
            parent[j][i] = parent[parent[j][i-1]][i-1];
        }
    }
}
int lca(int a, int b) {
    if (d1[a] > d1[b]) swap(a, b);
    for (int i = LOG-1; i >= 0; --i) {
        if ((d1[b] - d1[a]) >= ((ll)1 << i)) b = parent[b][i];
    }
    if (a == b) return a;
    for (int i = LOG-1; i >= 0; --i) {
        if (parent[a][i] != parent[b][i]) {
            a = parent[a][i];
            b = parent[b][i];
        }
    }
    return parent[a][0];
}
int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n-1; ++i) {
        int p, q, r;
        scanf("%d %d %d", &p, &q, &r);
        graph[p].push_back({q, r});
        graph[q].push_back({p, r});
    }
    set_parent();
    while (m--) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%lld\n", d[a] + d[b] - d[lca(a, b)] * 2);
    }
    return 0;
}