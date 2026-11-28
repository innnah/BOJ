#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

const int MAX = 100127;
int n, m, visited[MAX], parent[MAX], root[MAX], sz[MAX];
vector<int> tree[MAX], dist[21][MAX];
void dfs(int v) {
    visited[v] = 1;
    int cnt = 0;
    for (auto& i : tree[v]) {
        if (!visited[i]) {
            parent[i] = v;
            root[i] = cnt;
            dfs(i);
        }
        ++cnt;
    }
}
int main() {
    fastio;
    cin >> n >> m;
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
        ++sz[a]; ++sz[b];
    }
    dfs(1);
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j <= m; ++j) {
            dist[j][i] = vector<int>(sz[i] + 1, 0);
        }
    }
    for (int i = 1; i <= n; ++i) {
        int node = i;
        for (int j = 1; j <= m; ++j) {
            int pnode = parent[node];
            if (!pnode) break;
            ++dist[j][pnode][root[node]];
            ++dist[j][pnode][sz[pnode]];
            node = pnode;
        }
    }
    for (int i = 2; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            for (int k = 0; k <= sz[j]; ++k) {
                dist[i][j][k] += dist[i - 1][j][k];
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        int node = i, cand = 1;
        for (int j = 1; j <= m; ++j) {
            int pnode = parent[node];
            if (!pnode) break;
            cand += dist[m-j][pnode][sz[pnode]] - dist[m-j][pnode][root[node]] + 1;
            node = pnode;
        }
        cand += dist[m][i][sz[i]];
        ans = max(ans, cand);
    }
    cout << ans;
    return 0;
}