#include <bits/stdc++.h>

using namespace std;

long long tree[800080], visited[200010], s[200010], e[200010], d[200010];
int cnt = 0;
vector<int> graph[200010];

long long query(int le, int ri, int v, int s, int e) {
    if (le > e || ri < s) return 0;
    if (le <= s && e <= ri) return tree[v];
    int mid = (s + e) / 2;
    return query(le, ri, v * 2, s, mid) + query(le, ri, v * 2 + 1, mid + 1, e);
}

long long update(int idx, int v, int s, int e) {
    if (idx < s || idx > e) return tree[v];
    if (s == e) {
        ++tree[v];
        return tree[v];
    }
    int mid = (s + e) / 2;
    tree[v] = update(idx, v * 2, s, mid) + update(idx, v * 2 + 1, mid + 1, e);
    return tree[v];
}

void dfs(int v, int depth) {
    visited[v] = 1;
    d[v] = depth;
    s[v] = ++cnt;
    for (int i : graph[v]) {
        if (!visited[i]) {
            dfs(i, depth + 1);
        }
    }
    e[v] = cnt;
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n, c;
    cin >> n >> c;
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(c, 1);

    int q;
    cin >> q;
    while (q--) {
        int a, b;
        cin >> a >> b;
        if (a == 1) {
            update(s[b], 1, 1, n);
        } 
        else {
            cout << d[b] * query(s[b], e[b], 1, 1, n) << "\n";
        }
    }
    return 0;
}
