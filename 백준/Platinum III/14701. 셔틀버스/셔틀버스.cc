#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

int n, m, tree[801270];
int init(int v, int s, int e) {
    if (s == e) {
        tree[v] = 1;
        return tree[v];
    }
    int mid = (s + e) / 2;
    return tree[v] = init(v * 2, s, mid) + init(v * 2 + 1, mid + 1, e);
}
int query(int v, int s, int e, int l, int r) {
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree[v];
    int mid = (s + e) / 2;
    return tree[v] = query(v * 2, s, mid, l, r) + query(v * 2 + 1, mid + 1, e, l, r);
}
int query2(int v, int s, int e, int val) {
    if (s == e) return s;
    int mid = (s + e) / 2;
    if (val <= tree[v * 2]) return query2(v * 2, s, mid, val);
    return query2(v * 2 + 1, mid + 1, e, val - tree[v * 2]);
}
int update(int v, int s, int e, int idx, int val) {
    if (idx < s || e < idx) return tree[v];
    if (s == e) {
        tree[v] = val;
        return tree[v];
    }
    int mid = (s + e) / 2;
    return tree[v] = update(v * 2, s, mid, idx, val) + update(v * 2 + 1, mid + 1, e, idx, val);
}
int main() {
    fastio;
    cin >> n >> m;
    int start = -1, end = -2;
    init(1, 1, n);
    while (m--) {
        int a, b;
        cin >> a >> b;
        if (a == 1) {
            int sb = b;
            b = query(1, 1, n, 1, b);
            if (start == -1) {
                if (n % 2) start = end = (n + 1) / 2;
                else {
                    if (b <= n / 2) start = end = n / 2;
                    else start = end = n / 2 + 1;
                }
            }
            else {
                if (b < start) start -= 1;
                else end += 1;
            }
            update(1, 1, n, sb, 0);
        }
        else {
            if (start <= b && b <= end) {
                cout << 0 << endl;
                continue;
            }
            cout << query2(1, 1, n, b - (end - start + 1) * (b > end)) << endl;
        }
    }
    return 0;
}