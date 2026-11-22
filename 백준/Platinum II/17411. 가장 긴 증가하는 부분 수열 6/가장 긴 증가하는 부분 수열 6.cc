#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

struct dat {
    ll lis, cnt;
};

const ll MOD = 1000000007;
ll n, tarr[1001000], sarr[1001000], arr[1001000];
dat tree[4004000];
inline dat merge(dat& a, dat& b) {
    if (a.lis > b.lis) return a;
    if (a.lis < b.lis) return b;
    return {a.lis, (a.cnt + b.cnt) % MOD};
}
dat query(int l, int r, int v, int s, int e) {
    if (r < s || e < l) return {0, 0};
    if (l <= s && e <= r) return tree[v];
    int mid = (s + e) / 2;
    dat ls = query(l, r, v*2, s, mid), rs = query(l, r, v*2+1, mid+1, e);
    return merge(ls, rs);
}
dat update(int idx, dat val, int v, int s, int e) {
    if (idx < s || e < idx) return tree[v];
    if (s == e) {
        tree[v] = merge(val, tree[v]);
        return tree[v];
    }
    int mid = (s + e) / 2;
    dat ls = update(idx, val, v*2, s, mid), rs = update(idx, val, v*2+1, mid+1, e);
    return tree[v] = merge(ls, rs);
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> tarr[i];
        sarr[i] = tarr[i];
    }
    sort(sarr, sarr+n);
    for (int i = 0; i < n; ++i) {
        arr[i] = lower_bound(sarr, sarr+n, tarr[i]) - sarr;
    }
    for (int i = 0; i < n; ++i) {
        dat q = query(0, arr[i]-1, 1, 0, n-1);
        if (q.lis == 0) q = {0, 1};
        update(arr[i], {q.lis+1, q.cnt}, 1, 0, n-1);
    }
    cout << tree[1].lis << " " << tree[1].cnt;
    return 0;
}