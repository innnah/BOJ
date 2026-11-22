#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

int n, m, arr[100127], mnFactor[1000127], fcnt[1000127];
ll tree[401270], lazy[401270];
vector<ll> nums[401270];
void init(int v, int s, int e) {
    if (s == e) {
        tree[v] = arr[s];
        ll tmp = arr[s];
        nums[v] = vector<ll>(9);
        for (int i = 0; i < 9; ++i) {
            nums[v][i] = tmp;
            tmp = fcnt[tmp];
        }
        return;
    }
    int mid = (s + e) / 2;
    init(v * 2, s, mid); init(v * 2 + 1, mid + 1, e);
    tree[v] = tree[v * 2] + tree[v * 2 + 1];
    nums[v] = vector<ll>(9);
    for (int i = 0; i < 9; ++i) {
        nums[v][i] = nums[v * 2][i] + nums[v * 2 + 1][i];
    }
}
void lazy_update(int v, int s, int e) {
    if (lazy[v]) {
        int tmp = min(8LL, lazy[v]), tmp2 = nums[v][8];
        for (int i = tmp; i < 9; ++i) {
            nums[v][i - tmp] = nums[v][i];
        }
        for (int i = 9 - tmp; i < 9; ++i) {
            nums[v][i] = tmp2;
        }
        tree[v] = nums[v][0];
        if (s != e) {
            lazy[v * 2] += lazy[v];
            lazy[v * 2 + 1] += lazy[v];
        }
        lazy[v] = 0;
    }
}
ll query(int v, int s, int e, int l, int r) {
    lazy_update(v, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree[v];
    int mid = (s + e) / 2;
    ll ans = query(v * 2, s, mid, l, r) + query(v * 2 + 1, mid + 1, e, l, r);
    for (int i = 0; i < 9; ++i) {
        nums[v][i] = nums[v * 2][i] + nums[v * 2 + 1][i];
    }
    return ans;
}
ll update(int v, int s, int e, int l, int r) {
    lazy_update(v, s, e);
    if (r < s || e < l) return tree[v];
    if (l <= s && e <= r) {
        lazy[v] += 1;
        lazy_update(v, s, e);
        return tree[v];
    }
    int mid = (s + e) / 2;
    tree[v] = update(v * 2, s, mid, l, r) + update(v * 2 + 1, mid + 1, e, l, r);
    for (int i = 0; i < 9; ++i) {
        nums[v][i] = nums[v * 2][i] + nums[v * 2 + 1][i];
    }
    return tree[v];
}
int main() {
    fastio;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) cin >> arr[i];
    for (int i = 1; i <= 1000000; ++i) mnFactor[i] = i;
    for (int i = 2; i <= 1000; ++i) {
        if (mnFactor[i] == i) {
            for (int j = i * i; j <= 1000000; j += i) {
                mnFactor[j] = i;
            }
        }
    }
    fcnt[1] = 1;
    for (int i = 2; i <= 1000000; ++i) {
        int num = i, dcnt = 0;
        while (num % mnFactor[i] == 0) {
            ++dcnt;
            num /= mnFactor[i];
        }
        fcnt[i] = fcnt[num] * (dcnt + 1);
    }
    init(1, 0, n - 1);
    while (m--) {
        int q;
        cin >> q;
        if (q == 1) {
            int a, b;
            cin >> a >> b;
            --a; --b;
            update(1, 0, n - 1, a, b);
        }
        else {
            int a, b;
            cin >> a >> b;
            --a; --b;
            cout << query(1, 0, n - 1, a, b) << endl;
        }
    }
    return 0;
}