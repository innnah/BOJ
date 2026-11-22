#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>
#include <random>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt
#define pll pair<ll, ll>
#define pint pair<int, int>

const int MAX = 100000 + 10;
int n, m, visited[MAX], s[MAX], e[MAX], cnt = 0;
vector<int> graph[MAX];
struct lazy_segTree {
    ll seg[MAX * 4], lazy[MAX * 4], a[MAX];
    lazy_segTree(vector<ll> input) {
        for (int i = 0; i < input.size(); ++i) a[i] = input[i];
        init(1, 0, input.size() - 1);
        memset(lazy, -1, sizeof(lazy));
    };
    void lazy_update(int node, int s, int e) {
        if (lazy[node] != -1) {
            seg[node] ^= lazy[node] * ((e - s + 1) % 2);
            if (s != e) {
                if (lazy[node * 2] == -1) lazy[node * 2] = 0;
                if (lazy[node * 2 + 1] == -1) lazy[node * 2 + 1] = 0;
                lazy[node * 2] ^= lazy[node];
                lazy[node * 2 + 1] ^= lazy[node];
            }
            lazy[node] = -1;
        }
    }
    ll init(int node, int s, int e) {
        if (s == e) return seg[node] = a[s];
        int mid = (s + e) / 2;
        seg[node] = init(node * 2, s, mid) ^ init(node * 2 + 1, mid + 1, e);
        return seg[node];
    }
    ll query(int node, int s, int e, int l, int r) {
        lazy_update(node, s, e);
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return seg[node];
        int mid = (s + e) / 2;
        return query(node * 2, s, mid, l, r) ^ query(node * 2 + 1, mid + 1, e, l, r);
    }
    ll update(int node, int s, int e, int l, int r, ll diff) {
        lazy_update(node, s, e);
        if (r < s || e < l) return seg[node];
        if (l <= s && e <= r) {
            if (lazy[node] == -1) lazy[node] = 0;
            lazy[node] ^= diff;
            lazy_update(node, s, e);
            return seg[node];
        }
        int mid = (s + e) / 2;
        return seg[node] = update(node * 2, s, mid, l, r, diff) ^ update(node * 2 + 1, mid + 1, e, l, r, diff);
    }
};
void dfs(int v) {
    visited[v] = 1;
    s[v] = ++cnt;
    for (int i : graph[v]) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    e[v] = cnt;
}
int main() {
	fastio;
    cin >> n >> m;
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(1);
    vector<ll> tmp(n, 0);
    lazy_segTree* seg = new lazy_segTree(tmp);
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        seg->update(1, 0, n - 1, s[i+1]-1, s[i+1]-1, a);
    }
    while (m--) {
        int q;
        cin >> q;
        if (q == 1) {
            int a;
            cin >> a;
            cout << seg->query(1, 0, n - 1, s[a] - 1, e[a] - 1) << endl;
        }
        else {
            int a, b;
            cin >> a >> b;
            seg->update(1, 0, n - 1, s[a] - 1, e[a] - 1, b);
        }
    }
	return 0;
}