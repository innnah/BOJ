#include <bits/stdc++.h>
using namespace std;

static const int MAXN = 300127;
static const int LOG = 21;

int n;
vector<int> graph[MAXN+1];
int parent[MAXN+1][LOG], d[MAXN+1], cArr[MAXN+1], visited[MAXN+1];

void dfs(int v, int depth) {
    cArr[v] = 1;
    d[v] = depth;
    for(int nxt : graph[v]) {
        if(!cArr[nxt]) {
            parent[nxt][0] = v;
            dfs(nxt, depth + 1);
        }
    }
}

void set_parent() {
    dfs(1, 0);
    for(int i = 1; i < LOG; i++) {
        for(int v = 1; v <= n; v++) {
            parent[v][i] = parent[ parent[v][i-1] ][i-1];
        }
    }
}

int lca(int a, int b) {
    if(d[a] > d[b]) swap(a, b);
    for(int i = LOG - 1; i >= 0; i--) {
        if(d[b] - d[a] >= (1 << i)) {
            b = parent[b][i];
        }
    }

    if(a == b) return a;

    for(int i = LOG - 1; i >= 0; i--) {
        if(parent[a][i] != parent[b][i]) {
            a = parent[a][i];
            b = parent[b][i];
        }
    }
    return parent[a][0];
}

pair<int, int> dfs2(int v) {
    visited[v] = 1;
    int dist = 0;
    int farthest = v;

    for(int nxt : graph[v]) {
        if(!visited[nxt]) {
            auto cand = dfs2(nxt);
            if(dist < cand.first + 1) {
                dist = cand.first + 1;
                farthest = cand.second;
            }
        }
    }
    return {dist, farthest};
}

int getAns(int u, int v, int i) {
    int lca1 = lca(u, i);
    int lca2 = lca(v, i);
    int cand = d[u] + d[v] + 2*d[i] - 2*(d[lca1] + d[lca2]);
    return cand;
}

int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    cin >> n;
    for(int i=0; i<n-1; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    set_parent();

    memset(visited, 0, sizeof(visited));
    int b = dfs2(1).second;

    memset(visited, 0, sizeof(visited));
    int a = dfs2(b).second;
    
    int ans1 = -1;
    int x = -1;
    for(int i = 1; i <= n; i++){
        int cand = getAns(a, b, i);
        if(ans1 < cand){
            ans1 = cand;
            x = i;
        }
    }

    int q;
    cin >> q;
    while(q--){
        int u, v;
        cin >> u >> v;
        int ansVal = max({ getAns(u, v, a), getAns(u, v, b), getAns(u, v, x) });
        cout << ansVal << "\n";
    }

    return 0;
}
