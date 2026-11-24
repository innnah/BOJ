#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

const int MAX = 1000000 + 10;
int n, m;
struct lazy_segTree {
    ll seg[MAX * 4], lazy[MAX * 4], a[MAX];
    lazy_segTree(vector<ll> input) {
        for (int i = 0; i < input.size(); ++i) a[i] = input[i];
        init(1, 0, input.size() - 1);
        memset(lazy, 0, sizeof(lazy));
    };
    void lazy_update(int node, int s, int e) {
        if (lazy[node]) {
            seg[node] += (e - s + 1) * lazy[node];
            if (s != e) {
                lazy[node * 2] += lazy[node];
                lazy[node * 2 + 1] += lazy[node];
            }
            lazy[node] = 0;
        }
    }
    ll init(int node, int s, int e) {
        if (s == e) return seg[node] = a[s];
        int mid = (s + e) / 2;
        seg[node] = init(node * 2, s, mid) + init(node * 2 + 1, mid + 1, e);
        return seg[node];
    }
    ll query(int node, int s, int e, int l, int r) {
        lazy_update(node, s, e);
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return seg[node];
        int mid = (s + e) / 2;
        return query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r);
    }
    ll update(int node, int s, int e, int l, int r, ll diff) {
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
int main() {
    fastio;
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    lazy_segTree* seg = new lazy_segTree(a);
    cin >> m;
    for (int i = 0; i < m; ++i) {
        int a;
        cin >> a;
        if (a - 1) {
            int b, c;
            cin >> b >> c;
            cout << seg->query(1, 0, n - 1, b-1, c-1) << endl;
        }
        else {
            ll i, j, k;
            cin >> i >> j >> k;
            seg->update(1, 0, n - 1, i-1, j-1, k);
        }
    }
    return 0;
}