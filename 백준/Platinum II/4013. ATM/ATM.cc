#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

vector<int> graph[500500], rev_graph[500500], st, sccGraph[500500];
int visited[500500], sccId[500500], n, m, money[500500], s, p, res[500500], sccMoney[500500], indegree[500500], dp[500500];
void dfs(int v) {
    visited[v] = 1;
    for (auto& i : graph[v])
        if (!visited[i]) dfs(i);
    st.push_back(v);
}
void rev_dfs(int v, int Si) {
    visited[v] = 1;
    sccId[v] = Si;
    for (auto& i : rev_graph[v])
        if (!visited[i]) rev_dfs(i, Si);
}
int main() {
    fastio;
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        rev_graph[b].push_back(a);
    }
    for (int i = 0; i < n; ++i) {
        cin >> money[i];
    }
    cin >> s >> p;
    for (int i = 0; i < p; ++i) {
        cin >> res[i];
    }
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) dfs(i);
    }
    for (int i = 1; i <= n; ++i) visited[i] = 0;
    int cnt = 0;
    while (!st.empty()) {
        int node = st.back();
        st.pop_back();
        if (!visited[node]) rev_dfs(node, cnt++);
    }
    int g = cnt-1;
    for (int i = 1; i <= n; ++i) {
        sccMoney[sccId[i]] += money[i - 1];
    }
    for (int i = 1; i <= n; ++i) {
        for (auto& j : graph[i]) {
            if (sccId[i] != sccId[j]) {
                sccGraph[sccId[i]].push_back(sccId[j]);
                ++indegree[sccId[j]];
            }
        }
    }
    s = sccId[s];
    memset(dp, -1, sizeof(dp));
    for (auto& i : res) {
        dp[sccId[i]] = sccMoney[sccId[i]];
    }
    queue<int> q;
    for (int i = 0; i <= g; ++i) {
        if (indegree[i] == 0) q.push(i);
    }
    vector<int> ret;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        ret.push_back(v);
        for (auto& i : sccGraph[v]) {
            if (--indegree[i] == 0) q.push(i);
        }
    }
    for (int i = ret.size()-1; i >= 0; --i) {
        int val = ret[i];
        for (auto& j : sccGraph[val]) {
            if (dp[j] != -1) dp[val] = max(dp[val], dp[j] + sccMoney[val]);
        }
    }
    cout << dp[s];
    return 0;
}
