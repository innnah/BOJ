#include <bits/stdc++.h>
#define ll long long
#define endl "\n"

using namespace std;

int n, m, red, black, visited[100100], parent[100100];
pair<int, int> red_black_cnt[100100];
vector<int> tree[100100];
pair<int, int> dfs(int v, bool dis) {
    visited[v] = 1;
    int r = 0, b = 0;
    if (dis) b = 1;
    else r = 1;
    for (auto& i : tree[v]) {
        if (!visited[i]) {
            parent[i] = v;
            pair<int, int> sub = dfs(i, !dis);
            r += sub.first; b += sub.second;
        }
    }
    return red_black_cnt[v] = {r, b};
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n >> m;
    for (int i = 0; i < n-1; ++i) {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    dfs(1, 0);
    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;
        if (parent[a] != b) {
            int tmp = b;
            b = a;
            a = tmp;
        }
        long long ar = red_black_cnt[a].first, ab = red_black_cnt[a].second;
        long long br = red_black_cnt[1].first-ar, bb = red_black_cnt[1].second-ab;
        if (c) {
            cout << ar * bb + br * ab << endl;
        }
        else {
            cout << ar * br + ab * bb << endl;
        }
    }
    return 0;
}