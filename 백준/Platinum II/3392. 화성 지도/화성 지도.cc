#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAX = 524287;

ll n, rect[10127][4];
ll seg[2127152], cnt[2127152];
vector<ll> arr;

struct Query {
    ll when;
    pair<ll, ll> range;
    ll diff;
};

bool comp(const Query& a, const Query& b) {
    return a.when < b.when;
}

int getIdx(ll num) {
    return lower_bound(arr.begin(), arr.end(), num) - arr.begin();
}
void update(int node, int s, int e, int l, int r, ll diff) {
    if (r < s || e < l) return;
    if (l <= s && e <= r) {
        cnt[node] += diff;
    }
    else {
        int mid = (s + e) / 2;
        update(node * 2, s, mid, l, r, diff); update(node * 2 + 1, mid + 1, e, l, r, diff);
    }
    if (cnt[node]) seg[node] = arr[e] - arr[s - 1];
    else {
        if (s == e) seg[node] = 0;
        else seg[node] = seg[node * 2] + seg[node * 2 + 1];
    }
}
int main() {
    fastio;
    cin >> n;
    vector<Query> updates;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> rect[i][j];
        }
        ++rect[i][1]; ++rect[i][3];
        updates.push_back({ rect[i][0], {rect[i][1], rect[i][3]}, 1 });
        updates.push_back({ rect[i][2], {rect[i][1], rect[i][3]}, -1 });
        arr.push_back(rect[i][1]);
        arr.push_back(rect[i][3]);
    }
    sort(updates.begin(), updates.end(), comp);
    sort(arr.begin(), arr.end());
    arr.erase(unique(arr.begin(), arr.end()), arr.end());
    
    ll ans = 0;
    update(1, 1, MAX, getIdx(updates[0].range.first)+1, getIdx(updates[0].range.second), updates[0].diff);
    for (int i = 1; i < updates.size(); ++i) {
        ans += seg[1] * (updates[i].when - updates[i - 1].when);
        update(1, 1, MAX, getIdx(updates[i].range.first)+1, getIdx(updates[i].range.second), updates[i].diff);
    }
    cout << ans;
    return 0;
}