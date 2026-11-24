#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, sy, ex, naming_is_so_hard[100100][2];
ll dp[100100][2], visited[100100][2];
vector<int> blocker[100100];
vector<int> ans;
vector<int> tmp;
map<int, int> d;
map<int, int> revd;

ll tree[800800], lazy[800800], arr[200200];
void lazy_update(int v, int s, int e) {
    if (lazy[v] != -1) {
        tree[v] = lazy[v] * (e - s + 1);
        if (s != e) {
            lazy[v * 2] = lazy[v];
            lazy[v * 2 + 1] = lazy[v];
        }
        lazy[v] = -1;
    }
}
ll query(int l, int r, int v, int s, int e) {
    lazy_update(v, s, e);
    if (r < s || e < l) return 0;
    if (l <= s && e <= r) return tree[v];
    int mid = (s + e) / 2;
    return query(l, r, v * 2, s, mid) + query(l, r, v * 2 + 1, mid + 1, e);
}
ll update(int l, int r, int val, int v, int s, int e) {
    lazy_update(v, s, e);
    if (r < s || e < l) return tree[v];
    if (l <= s && e <= r) {
        lazy[v] = val;
        lazy_update(v, s, e);
        return tree[v];
    }
    int mid = (s + e) / 2;
    return tree[v] = update(l, r, val, v * 2, s, mid) + update(l, r, val, v * 2 + 1, mid + 1, e);
}

ll dpf(int idx, int y) {
    if (idx <= -1) return 0;
    int s = blocker[idx][1], e = blocker[idx][2];
    if (dp[idx][0] != -1) return min((ll)y - s + dp[idx][0], (ll)e - y + dp[idx][1]);
    ll& v1 = dp[idx][0];
    ll& v2 = dp[idx][1];
    v1 = dpf(naming_is_so_hard[idx][0]-1, s);
    v2 = dpf(naming_is_so_hard[idx][1]-1, e);
    return min(v1 + y - s, v2 + e - y);
}
void reconstruct(int idx, int y) {
    if (idx <= -1) {
        ans.push_back(y);
        return;
    }
    int s = blocker[idx][1], e = blocker[idx][2];
    int v1 = dpf(naming_is_so_hard[idx][0] - 1, s) + y - s, v2 = dpf(naming_is_so_hard[idx][1] - 1, e) + e - y;
    if (v1 <= v2) {
        if (!visited[idx][0]) {
            reconstruct(naming_is_so_hard[idx][0] - 1, s);
            visited[idx][0] = 1;
        }
    }
    if (v1 >= v2) {
        if (!visited[idx][1]) {
            reconstruct(naming_is_so_hard[idx][1] - 1, e);
            visited[idx][1] = 1;
        }
    }
}
int main() {
    fastio;
    memset(dp, -1, sizeof(dp));
    cin >> n >> sy >> ex;
    vector<vector<int>> input(n, vector<int>(3));
    tmp.push_back(sy);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 3; ++j) cin >> input[i][j];
        tmp.push_back(input[i][1]);
        tmp.push_back(input[i][2]);
        if (input[i][1] > input[i][2]) {
            swap(input[i][1], input[i][2]);
        }
    }
    stable_sort(input.begin(), input.end());
    stable_sort(tmp.begin(), tmp.end());
    int idx = 0;
    for (int i = 0; i < tmp.size(); ++i) {
        if (d.find(tmp[i]) == d.end()) {
            d.insert({ tmp[i], idx });
            revd.insert({ idx, tmp[i] });
            ++idx;
        }
    }
    idx = 1;
    blocker[0] = input[0];
    for (int i = 1; i < n; ++i) {
        blocker[i].resize(3);
        int s1 = blocker[idx - 1][1], s2 = input[i][1], e1 = blocker[idx - 1][2], e2 = input[i][2];
        if (blocker[idx - 1][0] == input[i][0] && !(s1 > e2 || s2 > e1)) {
            blocker[idx - 1][1] = min(s1, s2);
            blocker[idx - 1][2] = max(e1, e2);
        }
        else {
            blocker[idx++] = input[i];
        }
    }
    n = idx;
    memset(lazy, -1, sizeof(lazy));
    for (int i = n-1; i >= 0; --i) {
        int s = d[blocker[i][1]], e = d[blocker[i][2]];
        naming_is_so_hard[i][0] = query(s, s, 1, 0, tmp.size());
        naming_is_so_hard[i][1] = query(e, e, 1, 0, tmp.size());
        if (naming_is_so_hard[i][0] == 0) naming_is_so_hard[i][0] = -1;
        if (naming_is_so_hard[i][1] == 0) naming_is_so_hard[i][1] = -1;
        update(s, e, i+1, 1, 0, tmp.size());
    }
    int v = query(d[sy], d[sy], 1, 0, tmp.size());
    cout << dpf(v-1, sy) + ex << endl;
    reconstruct(query(d[sy], d[sy], 1, 0, tmp.size())-1, sy);
    sort(ans.begin(), ans.end());
    cout << ans.size() << " ";
    for (auto& i : ans) {
        cout << i << " ";
    }
    return 0;
}