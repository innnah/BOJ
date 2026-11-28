#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

const int MAX = 300127;
vector<int> tree1[MAX], tree2[MAX];
int visited[MAX], trace[MAX], n0[MAX];
int best, best_node;

void dfs1(int v, int depth) {
    visited[v] = 1;
    if (best < depth) {
        best = depth;
        best_node = v;
    }
    for (int& i : tree1[v]) {
        if (!visited[i]) {
            dfs1(i, depth + 1);
        }
    }
}

int dfs2(int v) {
    visited[v] = 1;
    int max_depth = 0;
    for (int& i : tree1[v]) {
        if (!visited[i]) {
            int cand = dfs2(i);
            if (max_depth < cand) {
                trace[v] = i;
                max_depth = cand;
            }
        }
    }
    return max_depth + 1;
}

void dfs3(int v, int depth) {
    visited[v] = 1;
    best = max(best, depth);
    for (int& i : tree2[v]) {
        if (!visited[i]) {
            dfs3(i, depth + 1);
        }
    }
}

int main() {
    fastio;
    int n;
    cin >> n;
    for (int i = 1; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        tree1[a].push_back(b);
        tree1[b].push_back(a);
    }

    memset(visited, 0, sizeof(visited));
    best = 0;
    best_node = 1;
    dfs1(1, 0);

    memset(visited, 0, sizeof(visited));
    dfs2(best_node);

    memset(n0, 0, sizeof(n0));
    int cnt = 1;
    n0[best_node] = 1;
    int last = best_node;
    while (trace[last] != 0) {
        n0[trace[last]] = 1;
        last = trace[last];
        cnt += 1;
    }

    for (int i = 1; i <= n; ++i) {
        int idx = i;
        if (n0[i]) idx = 0;
        for (int j : tree1[i]) {
            if (n0[j]) tree2[idx].push_back(0);
            else tree2[idx].push_back(j);
        }
    }

    memset(visited, 0, sizeof(visited));
    best = 0;
    dfs3(0, 0);

    if (best == 0) {
        cout << 0;
    }
    else {
        cout << best + cnt;
    }
    return 0;
}