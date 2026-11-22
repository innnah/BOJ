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

struct Range {
    ll start, end, step;
    Range operator+(Range& other);
};

Range Range::operator+(Range& other) {
    Range newR = { start + other.start, end + other.end, step + other.step };
    return newR;
}

ll n, seg[400010], arr[100010];
Range lazy[400010];
void lazy_update(int node, int s, int e) {
    if (lazy[node].step != 0) {
        seg[node] += (e - s + 1) * (lazy[node].end + lazy[node].start) / 2;
        if (s != e) {
            int mid = (s + e) / 2;
            Range left = { lazy[node].start, lazy[node].start + lazy[node].step * (mid - s), lazy[node].step };
            Range right = { left.end + left.step, lazy[node].end, lazy[node].step };
            lazy[node * 2] = lazy[node * 2] + left;
            lazy[node * 2 + 1] = lazy[node * 2 + 1] + right;
        }
        lazy[node] = { 0, 0, 0 };
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
        Range add = { s-l+1, s-l+e-s+1, 1 };
        lazy[node] = lazy[node] + add;
        lazy_update(node, s, e);
        return seg[node];
    }
    int mid = (s + e) / 2;
    return seg[node] = update(node * 2, s, mid, l, r) + update(node * 2 + 1, mid + 1, e, l, r);
}

int main() {
	fastio;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    init(1, 0, n - 1);
    int q;
    cin >> q;
    while (q--) {
        int qType;
        cin >> qType;
        if (qType == 1) {
            int left, right;
            cin >> left >> right;
            update(1, 0, n - 1, left - 1, right - 1);
        }
        else {
            int pos;
            cin >> pos;
            cout << query(1, 0, n - 1, pos - 1, pos - 1) << endl;
        }
    }
	return 0;
}