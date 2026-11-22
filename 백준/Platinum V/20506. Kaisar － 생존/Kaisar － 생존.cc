#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int n;
long long dp[200200];
vector<int> tree[200200];
int dfs(int v) {
    long long ret = 0;
    int nodes = 1;
    for (auto& i : tree[v]) {
        int sub = dfs(i);
        ret += (long long)sub*sub;
        nodes += sub;
    }
    dp[v] = (long long)nodes*nodes - ret;
    return nodes;
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n;
    int root = 0;
    for (int i = 1; i <= n; ++i) {
        int a;
        cin >> a;
        tree[a].push_back(i);
        if (!a) root = i;
    }
    dfs(root);
    long long o = 0, e = 0;
    bool ended_odd = false;
    for (int i = 1; i <= n; ++i) {
        if (ended_odd) {
            e += (dp[i]+1)/2*i;
            o += dp[i]/2*i;
        }
        else {
            o += (dp[i]+1)/2*i;
            e += dp[i]/2*i;
        }
        if (dp[i] % 2) ended_odd = !ended_odd;
    }
    cout << e << " " << o;
    return 0;
}