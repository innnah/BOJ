#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const ll MOD = 1000000007;
ll seg[4000010], lazy1[4000010], lazy2[4000010], arr[1000010];
int n, q;
void lazy_update(int node, int s, int e) {
    if (!(lazy1[node] == 1 && lazy2[node] == 0)) {
        seg[node] = seg[node] * lazy1[node] + (ll)(e - s + 1) * lazy2[node];
        seg[node] %= MOD;
        if (s != e) {
            for (int i = 0; i < 2; ++i) {
                lazy1[node * 2 + i] *= lazy1[node];
                lazy2[node * 2 + i] *= lazy1[node];
                lazy2[node * 2 + i] += lazy2[node];
                lazy1[node * 2 + i] %= MOD;
                lazy2[node * 2 + i] %= MOD;
            }
        }
        lazy1[node] = 1;
        lazy2[node] = 0;
    }
}
ll init(int node, int s, int e) {
    lazy1[node] = 1;
    if (s == e) return seg[node] = arr[s];
    int mid = (s + e) / 2;
    seg[node] = (init(node * 2, s, mid) + init(node * 2 + 1, mid + 1, e)) % MOD;
    return seg[node];
}
ll query(int node, int s, int e, int l, int r) {
    lazy_update(node, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg[node];
    int mid = (s + e) / 2;
    return (query(node * 2, s, mid, l, r) + query(node * 2 + 1, mid + 1, e, l, r)) % MOD;
}
ll update1(int node, int s, int e, int l, int r, ll diff) {
    lazy_update(node, s, e);
    if (r < s || e < l) return seg[node];
    if (l <= s && e <= r) {
        lazy2[node] += diff;
        lazy2[node] %= MOD;
        lazy_update(node, s, e);
        return seg[node] %= MOD;
    }
    int mid = (s + e) / 2;
    return seg[node] = (update1(node * 2, s, mid, l, r, diff) + update1(node * 2 + 1, mid + 1, e, l, r, diff)) % MOD;
}
ll update2(int node, int s, int e, int l, int r, ll diff) {
    lazy_update(node, s, e);
    if (r < s || e < l) return seg[node];
    if (l <= s && e <= r) {
        lazy1[node] *= diff;
        lazy2[node] *= diff;
        lazy1[node] %= MOD;
        lazy2[node] %= MOD;
        lazy_update(node, s, e);
        return seg[node] %= MOD;
    }
    int mid = (s + e) / 2;
    return seg[node] = (update2(node * 2, s, mid, l, r, diff) + update2(node * 2 + 1, mid + 1, e, l, r, diff)) % MOD;
}
int main() {
    fastio;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    init(1, 0, n - 1);
    cin >> q;
    while (q--) {
        int qtype;
        cin >> qtype;
        if (qtype == 1) {
            int a, b, c;
            cin >> a >> b >> c;
            update1(1, 0, n - 1, a - 1, b - 1, c);
        }
        else if (qtype == 2) {
            int a, b, c;
            cin >> a >> b >> c;
            update2(1, 0, n - 1, a - 1, b - 1, c);
        }
        else if (qtype == 3) {
            int a, b, c;
            cin >> a >> b >> c;
            update2(1, 0, n - 1, a - 1, b - 1, 0);
            update1(1, 0, n - 1, a - 1, b - 1, c);
        }
        else {
            int a, b;
            cin >> a >> b;
            cout << query(1, 0, n - 1, a - 1, b - 1) % MOD << endl;
        }
    }
    return 0;
}