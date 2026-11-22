#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

ll n, k, seg[401270], lazy[401270], arr[100127];
void lazy_update(int node, int s, int e) {
    if (lazy[node]) {
        seg[node] += lazy[node];
        if (s != e) {
            lazy[node * 2] += lazy[node];
            lazy[node * 2 + 1] += lazy[node];
        }
        lazy[node] = 0;
    }
}
ll query(int node, int s, int e, int l, int r) {
    lazy_update(node, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg[node];
    int mid = (s + e) / 2;
    return max(query(node * 2, s, mid, l, r), query(node * 2 + 1, mid + 1, e, l, r));
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
    return seg[node] = max(update(node * 2, s, mid, l, r, diff), update(node * 2 + 1, mid + 1, e, l, r, diff));
}
int main() {
	fastio;
    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
    }
    ll ret = 0;
    for (int i = 1; i <= k; ++i) {
        update(1, 0, n, i, k, arr[i]);
        if (i != 1) update(1, 0, n, 0, i - 2, arr[i]);
    }
    for (int i = k + 1; i <= n; ++i) {
        update(1, 0, n, 0, i - 2, arr[i]);
        update(1, 0, n, 0, i - k - 2, -arr[i - k]);
        ll qval = query(1, 0, n, 0, i - 2);
        ret = max(ret, qval);
        update(1, 0, n, i, i, qval);
    }
    cout << ret;
	return 0;
}