#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAX = 100000 + 10;
int n, m;
int s[MAX], e[MAX], cnt = 0;
vector<int> graph[MAX];
template<typename T>
struct lazy_segTree {
    T seg[MAX * 4], lazy[MAX * 4], a[MAX];
    lazy_segTree(vector<T> input) {
        for (int i = 0; i < input.size(); ++i) a[i] = input[i];
        init(1, 0, input.size() - 1);
        memset(lazy, 0, sizeof(lazy));
    };
    void lazy_update(int node, int s, int e) {
        if (lazy[node]) {
            seg[node] += (e-s+1) * lazy[node];
            if (s != e) {
                lazy[node * 2] += lazy[node];
                lazy[node * 2 + 1] += lazy[node];
            }
            lazy[node] = 0;
        }
    }
    T init(int node, int s, int e) {
        if (s == e) return seg[node] = a[s];
        int mid = (s + e) / 2;
        seg[node] = init(node * 2, s, mid) + init(node * 2 + 1, mid + 1, e);
        return seg[node];
    }
    T query(int node, int s, int e, int l, int r) {
        lazy_update(node, s, e);
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return seg[node];
        int mid = (s + e) / 2;
        return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r);
    }
    T update(int node, int s, int e, int l, int r, T diff) {
        lazy_update(node, s, e);
        if (r < s || e < l) return seg[node];
        if (l <= s && e <= r) {
            lazy[node] += diff;
            lazy_update(node, s, e);
            return seg[node];
        }
        int mid = (s + e) / 2;
        return seg[node] = update(node * 2, s, mid, l, r, diff) + update(node * 2 + 1, mid + 1, e, l, r, diff);
    }
};
void dfs(int v, int a) {
    s[v] = ++cnt;
    for (int next : graph[v]) {
        if (next == a) continue;
        dfs(next, v);
    }
    e[v] = cnt;
}
int main() {
    fastio;
    cin >> n >> m;
    int a;
    cin >> a;
    for (int i = 1; i < n; ++i) {
        cin >> a;
        graph[a].push_back(i + 1);
    }
    vector<int> tmp(n, 0);
    dfs(1, -1);
    lazy_segTree<int> *seg = new lazy_segTree<int>(tmp), *seg2 = new lazy_segTree<int>(tmp);
    int mode = 0;
    while (m--) {
        cin >> a;
        if (a == 1) {
            int b, c;
            cin >> b >> c;
            if (mode) seg2->update(1, 0, n - 1, s[b]-1, s[b]-1, c);
            else seg->update(1, 0, n - 1, s[b]-1, e[b]-1, c);
        }
        else if (a == 2) {
            int b;
            cin >> b;
            cout << seg->query(1, 0, n - 1, s[b]-1, s[b]-1) + seg2->query(1, 0, n-1, s[b]-1, e[b]-1) << endl;
        }
        else {
            mode = ~mode;
        }
    }
    return 0;
}