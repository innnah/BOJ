#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> graph[MAXN];
int parents[MAXN], depth[MAXN], sz[MAXN], enter[MAXN], out[MAXN], top[MAXN], seg[4*MAXN];
int n, q, pv = 0;

void update(int idx, int val, int v, int s, int e) {
    if (idx < s || idx > e) return;
    if (s == e) {
        seg[v] += val;
        return;
    }
    int mid = (s + e) / 2;
    if (idx <= mid) update(idx, val, v*2, s, mid);
    else update(idx, val, v*2+1, mid+1, e);
    seg[v] = seg[v*2] + seg[v*2+1];
}
int query(int l, int r, int v, int s, int e) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg[v];
    int mid = (s + e) / 2;
    return query(l, r, v*2, s, mid) + query(l, r, v*2+1, mid+1, e);
}

void dfs1(int v) {
    sz[v] = 1;
    for (size_t idx = 0; idx < graph[v].size(); ++idx) {
        int i = graph[v][idx];
        depth[i] = depth[v] + 1;
        dfs1(i);
        sz[v] += sz[i];
        if (sz[i] > sz[graph[v][0]]) {
            swap(graph[v][0], graph[v][idx]);
        }
    }
}
void dfs2(int v) {
    enter[v] = ++pv;
    for (int i : graph[v]) {
        top[i] = (i == graph[v][0]) ? top[v] : i;
        dfs2(i);
    }
    out[v] = pv;
}

void hld_update(int idx, int val) {
    update(enter[idx], val, 1, 1, n);
}
int hld_query(int a, int b) {
    int ret = 0;
    while (top[a] != top[b]) {
        if (depth[top[a]] < depth[top[b]]) swap(a, b);
        ret += query(enter[top[a]], enter[a], 1, 1, n);
        a = parents[top[a]];
    }
    if (depth[a] > depth[b]) swap(a, b);
    ret += query(enter[a], enter[b], 1, 1, n) - query(enter[a], enter[a], 1, 1, n);
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

    cin >> n >> q;
    parents[1] = 0;
    for (int i = 2; i <= n; ++i) {
        cin >> parents[i];
        graph[parents[i]].push_back(i);
    }

    depth[1] = 1;
    top[1] = 1;
    dfs1(1);
    dfs2(1);

    for (int i = 0; i < q; ++i) {
        int a, b, t;
        cin >> a >> b >> t;
        int qr = hld_query(a, b);
        if (qr) {
            cout << "NO\n";
            if (t) hld_update(b, 1);
        } else {
            cout << "YES\n";
            if (t) hld_update(a, 1);
        }
    }
    return 0;
}
