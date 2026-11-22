#include <bits/stdc++.h>
using namespace std;
int n, m, dp[1002], trace[1002];
vector<pair<int, int>> graph[1002];
int dpf(int node) {
    if (node == 0) return 0;
    int& ret = dp[node];
    if (ret != -1) return ret;
    ret = 0;
    for (auto& ne : graph[node]) {
        int nnode = ne.first, score = ne.second;
        if (nnode == 1) {
            if (ret < score) {
                trace[node] = nnode;
                ret = score;
            }
        }
        else {
            int cand = score+dpf(nnode);
            if (ret < cand) {
                trace[node] = nnode;
                ret = cand;
            }
        }
    }
    return ret;
}
void reconstruct(int node) {
    if (node == 0) return;
    cout << node << " ";
    if (trace[node] != 1) reconstruct(trace[node]);
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    memset(dp, -1, sizeof(dp));
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b,c});
    }
    cout << dpf(1) << endl;
    reconstruct(1);
    cout << 1;
    return 0;
}