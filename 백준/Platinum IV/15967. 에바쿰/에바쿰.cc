#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

ll seg[4000010], lazy[4000010], arr[1000010];
int n, q1, q2;
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
int main() {
    fastio;
    cin >> n >> q1 >> q2;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    init(1, 0, n - 1);
    for (int i = 0; i < q1 + q2; ++i) {
        int a;
        cin >> a;
        if (a - 1) {
            int b, c;
            ll d;
            cin >> b >> c >> d;
            update(1, 0, n - 1, b - 1, c - 1, d);
        }
        else {
            int b, c;
            cin >> b >> c;
            cout << query(1, 0, n - 1, b - 1, c - 1) << endl;
        }
    }
    return 0;
}