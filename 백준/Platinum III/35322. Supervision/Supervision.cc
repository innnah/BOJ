#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

const ll MOD = 1000000007;
ll seg[2100000], lazy1[2100000], lazy2[2100000];
int n, d, cutlines[1012700], roles[1012700];
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
    if (s == e) return seg[node] = 1;
    int mid = (s + e) / 2;
    seg[node] = (init(node*2, s, mid) + init(node*2+1, mid+1, e)) % MOD;
    return seg[node];
}
ll query(int node, int s, int e, int l, int r) {
    lazy_update(node, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return seg[node];
    int mid = (s + e) / 2;
    return (query(node*2, s, mid, l, r) + query(node*2+1, mid+1, e, l, r)) % MOD;
}
ll update_add(int node, int s, int e, int l, int r, ll diff) {
    lazy_update(node, s, e);
    if (r < s || e < l) return seg[node];
    if (l <= s && e <= r) {
        lazy2[node] += diff;
        lazy2[node] %= MOD;
        lazy_update(node, s, e);
        return seg[node] %= MOD;
    }
    int mid = (s + e) / 2;
    return seg[node] = (update_add(node*2, s, mid, l, r, diff) + update_add(node*2+1, mid+1, e, l, r, diff)) % MOD;
}
ll update_mul(int node, int s, int e, int l, int r, ll diff) {
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
    return seg[node] = (update_mul(node*2, s, mid, l, r, diff) + update_mul(node*2+1, mid+1, e, l, r, diff)) % MOD;
}
int main() {
	fastio;
	cin >> n >> d;
	queue<pii> q;
	int cnt = 0;
	for (int i = 1; i <= n; ++i) {
		int p, o;
		cin >> p >> o;
		roles[i] = o;
		if (o) {
			q.push({++cnt, p+d});
		}
		else {
			while (!q.empty() && q.front().second < p) q.pop();
			if (!q.empty()) cutlines[i] = q.front().first;
			else cutlines[i] = MOD;
		}
	}
	init(1, 0, cnt);
	int cnt2 = cnt;
	for (int i = n; i >= 1; --i) {
		if (roles[i]) {
			//cout << query(1, 0, cnt, cnt2, cnt2) << endl;
			update_add(1, 0, cnt, 0, cnt2-1, query(1, 0, cnt, cnt2, cnt2));
			cnt2--;
		}
		else {
			if (cutlines[i] != MOD) update_mul(1, 0, cnt, cutlines[i], cnt2, 2);
			//cout << cutlines[i] << " " << cnt2 << endl;
		}
	}
	cout << (query(1, 0, cnt, 0, 0)-1+MOD) % MOD;
	return 0;
}