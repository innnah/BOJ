#include <bits/stdc++.h>
using namespace std;

const int INF = 200000000;
vector<int> tree;

int query(int l, int r, int v, int s, int e) {
    if (l <= s && e <= r) return tree[v];
    if (r < s || e < l) return INF;
    int mid = (s + e) / 2;
    return min(query(l, r, v*2, s, mid), query(l, r, v*2+1, mid+1, e));
}

int update(int idx, int val, int v, int s, int e) {
    if (idx < s || e < idx) return tree[v];
    if (s == e) {
        tree[v] = min(tree[v], val);
        return tree[v];
    }
    int mid = (s + e) / 2;
    tree[v] = min(update(idx, val, v*2, s, mid), update(idx, val, v*2+1, mid+1, e));
    return tree[v];
}

int main() {
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int n, q;
    cin >> n >> q;
    vector<vector<int>> meats(n, vector<int>(3));
    vector<vector<int>> querys(q, vector<int>(2));
    vector<int> sd;

    for (auto& meat : meats) {
        for (int& m : meat) cin >> m;
    }
    for (auto& query : querys) {
        for (int& q : query) cin >> q;
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 2; ++j) {
            sd.push_back(meats[i][j]);
            sd.push_back(meats[i][j]-1);
        }
    }
    for (int i = 0; i < q; ++i) {
        for (int j = 0; j < 2; ++j) {
            sd.push_back(querys[i][j]);
            sd.push_back(querys[i][j]-1);
        }
    }

    sort(sd.begin(), sd.end());
    sd.erase(unique(sd.begin(), sd.end()), sd.end());

    map<int, int> d;
    for (int i = 0; i < sd.size(); ++i) {
        d[sd[i]] = i;
    }
    for (auto& meat : meats) {
        meat[0] = d[meat[0]];
        meat[1] = d[meat[1]];
    }
    for (auto& query : querys) {
        for (int& q : query) q = d[q];
    }

    tree.assign(sd.size() * 4 + 8, INF);
    for (int i = 0; i < q; ++i) {
        update(querys[i][0], i, 1, 0, sd.size() - 1);
        update(querys[i][1], i, 1, 0, sd.size() - 1);
    }

    vector<long long> ans(q, 0);
    for (auto& meat : meats) {
        int v = query(meat[0], meat[1]-1, 1, 0, sd.size()-1);
        if (v < q && meat[0] <= querys[v][0] && querys[v][1] < meat[1]) {
            ans[v] += (long long)meat[2];
        }
    }
    for (auto& i : ans) {
        cout << i << '\n';
    }
    return 0;
}