#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

struct Query {
    int a, b, c, idx;
};

int n, q, ans[100100];
pair<int, int> arr[100100];
vector<int> tree[100100], firsts, t[100100];
Query querys[100100];
void update(int x, int y, int val) {
    x = upper_bound(firsts.begin(), firsts.end(), x) - firsts.begin();
    while (x <= n) {
        int idx = upper_bound(t[x].begin(), t[x].end(), y) - t[x].begin();
        while (idx <= t[x].size()) {
            tree[x][idx] += val;
            idx += (idx & -idx);
        }
        x += (x & -x);
    }
}

int query(int x, int y) {
    x = upper_bound(firsts.begin(), firsts.end(), x) - firsts.begin();
    int ret = 0;
    while (x > 0) {
        int idx = upper_bound(t[x].begin(), t[x].end(), y) - t[x].begin();
        while (idx > 0) {
            ret += tree[x][idx];
            idx -= (idx & -idx);
        }
        x -= (x & -x);
    }
    return ret;
}
int main() {
    fastio;
    cin >> n >> q;
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i].first >> arr[i].second;
        firsts.push_back(arr[i].first);
    }
    sort(firsts.begin(), firsts.end());
    for (int i = 1; i <= n; ++i) {
        int idx = upper_bound(firsts.begin(), firsts.end(), arr[i].first) - firsts.begin();
        while (idx <= n) {
            t[idx].push_back(arr[i].second);
            idx += (idx & -idx);
        }
    }
    for (int i = 1; i <= n; ++i) {
        tree[i].resize(t[i].size() + 10);
        sort(t[i].begin(), t[i].end());
    }
    sort(arr + 1, arr + n + 1, [](pair<int, int> a, pair<int, int> b) {
        return a.first + a.second > b.first + b.second;
    });
    for (int i = 1; i <= q; ++i) {
        cin >> querys[i].a >> querys[i].b >> querys[i].c;
        querys[i].idx = i;
    }
    sort(querys + 1, querys + q + 1, [](Query x, Query y) {
        return x.c > y.c;
    });
    int idx = 1;
    for (int i = 1; i <= q; ++i) {
        while (idx <= n && arr[idx].first + arr[idx].second >= querys[i].c) {
            update(arr[idx].first, arr[idx].second, 1);
            ++idx;
        }
        ans[querys[i].idx] = query(1000000000, 1000000000)
            - query(1000000000, querys[i].b - 1) - query(querys[i].a - 1, 1000000000)
            + query(querys[i].a - 1, querys[i].b - 1);
    }
    for (int i = 1; i <= q; ++i) {
        cout << ans[i] << endl;
    }
    return 0;
}