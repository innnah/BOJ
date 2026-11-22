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

int n, m;
ll seg[400010], arr[100010];
bool lazy[400010];
void lazy_update(int node, int s, int e) {
    if (lazy[node]) {
        seg[node] = (e - s + 1) - seg[node];
        if (s != e) {
            lazy[node * 2] = !lazy[node * 2];
            lazy[node * 2 + 1] = !lazy[node * 2 + 1];
        }
        lazy[node] = 0;
    }
}
ll init(int node, int s, int e) {
    if (s == e) return seg[node] = arr[s];
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
ll update(int node, int s, int e, int l, int r) {
    lazy_update(node, s, e);
    if (r < s || e < l) return seg[node];
    if (l <= s && e <= r) {
        lazy[node] = !lazy[node];
        lazy_update(node, s, e);
        return seg[node];
    }
    int mid = (s + e) / 2;
    return seg[node] = update(node * 2, s, mid, l, r) + update(node * 2 + 1, mid + 1, e, l, r);
}

int main() {
	fastio;
    cin >> n >> m;
    while (m--) {
        int q;
        cin >> q;
        if (q) {
            int a, b;
            cin >> a >> b;
            cout << query(1, 0, n - 1, a - 1, b - 1) << endl;
        }
        else {
            int a, b;
            cin >> a >> b;
            update(1, 0, n - 1, a - 1, b - 1);
        }
    }
	return 0;
}