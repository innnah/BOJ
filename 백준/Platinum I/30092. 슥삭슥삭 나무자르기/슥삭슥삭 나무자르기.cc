#include<bits/stdc++.h>

using namespace std;

const int MAX = 100127;

vector<int> edge[MAX], tree[MAX];
int top[MAX], in[MAX], parent[MAX], depth[MAX], sz[MAX];
int seg[1 << 18], lazy[1 << 18];
int n, q;

void dfs1(int v) {
    sz[v] = 1;
    for (int& i : edge[v])
        if (!sz[i]) {
            depth[i] = depth[v] + 1;
            parent[i] = v;
            dfs1(i);
            sz[v] += sz[i];
            tree[v].push_back(i);
            if (sz[tree[v][0]] < sz[i]) swap(tree[v][0], tree[v].back());
        }
}
int cur;
void dfs2(int v) {
    in[v] = ++cur;
    for (int& i : tree[v]) {
        top[i] = i != tree[v][0] ? i : top[v];
        dfs2(i);
    }
}
void lazy_update(int n, int s, int e) {
    if (lazy[n]) {
        seg[n] += lazy[n];
        if (s != e) {
            lazy[n*2] += lazy[n];
            lazy[n*2+1] += lazy[n];
        }
        lazy[n] = 0;
    }
}
int segUpdate(int v, int s, int e, int l, int r, int val) {
    lazy_update(v, s, e);
    if (r < s || e < l) return seg[v];
    if (l <= s && e <= r) {
        lazy[v] += val;
        lazy_update(v, s, e);
        return seg[v];
    }
    int mid = s + e >> 1;
    return seg[v] = segUpdate(v*2, s, mid, l, r, val) + segUpdate(v*2+1, mid + 1, e, l, r, val);
}
int segQuery(int v, int s, int e, int l, int r) {
    lazy_update(v, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg[v];
    int mid = s + e >> 1;
    return segQuery(v*2, s, mid, l, r) + segQuery(v*2+1, mid + 1, e, l, r);
}
void hldUpdate(int x, int y, int val) {
    while (top[x] ^ top[y]) {
        if (depth[top[x]] < depth[top[y]]) swap(x, y);
        segUpdate(1, 1, n, in[top[x]], in[x], val);
        x = parent[top[x]];
    }
    if (depth[x] > depth[y]) swap(x, y);
    segUpdate(1, 1, n, in[x] + 1, in[y], val);
}
int hldQuery(int x, int y) {
    while (top[x] ^ top[y]) {
        if (depth[top[x]] < depth[top[y]]) swap(x, y);
        if (segQuery(1, 1, n, in[top[x]], in[x])) return 1;
        x = parent[top[x]];
    }
    if (depth[x] > depth[y]) swap(x, y);
    return segQuery(1, 1, n, in[x] + 1, in[y]);
}

int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> n >> q;
    for (int i = 0; i < n-1; ++i) {
        int a, b;
        cin >> a >> b;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    dfs1(1); dfs2(1);
    while (q--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        hldUpdate(a, b, 1);
        cout << (hldQuery(c, d) ? "NO" : "YES") << "\n";
        hldUpdate(a, b, -1);
    }
    return 0;
}
