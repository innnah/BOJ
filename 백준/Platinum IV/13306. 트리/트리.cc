#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int unionfind[200005], parent[200005], n, q;
vector<vector<pair<int, int>>> query;
vector<int> update;
vector<bool> answer;
int find(int v) {
    if (v == unionfind[v]) return v;
    return unionfind[v] = find(unionfind[v]);
}
void unio(int u, int v) {
    u = find(u);
    v = find(v);
    unionfind[v] = unionfind[u];
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n >> q;
    unionfind[1] = 1;
    for (int i = 2; i <= n; ++i) {
        int p;
        cin >> p;
        parent[i] = p;
        unionfind[i] = i;
    }
    query.push_back({});
    for (int i = 0; i < q+n-1; ++i) {
        int order;
        cin >> order;
        if (order) {
            int a, b;
            cin >> a >> b;
            query[query.size()-1].push_back({a, b});
        }
        else {
            int a;
            cin >> a;
            update.push_back(a);
            query.push_back({});
        }
    }
    vector<int> tmp = update;
    stable_sort(tmp.begin(), tmp.end());
    int node = 1;
    for (auto i : tmp) {
        while (node < i) {
            unio(node, parent[node]);
            node += 1;
        }
        node += 2;
    }
    int queryidx = query.size()-1;
    int updateidx = update.size()-1;
    while (queryidx >= 0) {
        for (int i = query[queryidx].size()-1; i >= 0; --i) {
            answer.push_back(find(query[queryidx][i].first) == find(query[queryidx][i].second));
        }
        unio(update[updateidx], parent[update[updateidx]]);
        updateidx--;
        queryidx--;
    }
    for (int i = answer.size()-1; i >= 0; --i) {
        if (answer[i]) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
    return 0;
}