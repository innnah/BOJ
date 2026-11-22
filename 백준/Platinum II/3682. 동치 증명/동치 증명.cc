#include <bits/stdc++.h>

using namespace std;

int n, m, cnt = 0, visited[20127], sccId[20127];
vector<int> graph[20127], rgraph[20127], sccGraph[20127];
vector<vector<int>> scc;
stack<int> s;

void kosa(int v) {
    visited[v] = 1;
    for (int i : graph[v]) {
        if (!visited[i]) {
            kosa(i);
        }
    }
    s.push(v);
}

void raju(int v) {
    visited[v] = 1;
    scc[cnt].push_back(v);
    sccId[v] = cnt;
    for (int i : rgraph[v]) {
        if (!visited[i]) {
            raju(i);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        
        memset(visited, 0, sizeof(visited));
        memset(sccId, 0, sizeof(sccId));
        scc.clear();
        
        for (int i = 1; i <= n; ++i) {
            graph[i].clear();
            rgraph[i].clear();
            sccGraph[i].clear();
        }
        
        cnt = 0;
        
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
        }

        for (int i = 1; i <= n; ++i) {
            if (!visited[i]) {
                kosa(i);
            }
        }

        for (int i = 1; i <= n; ++i) {
            for (int j : graph[i]) {
                rgraph[j].push_back(i);
            }
        }

        memset(visited, 0, sizeof(visited));
        while (!s.empty()) {
            int v = s.top();
            s.pop();
            if (!visited[v]) {
                scc.push_back(vector<int>());
                raju(v);
                ++cnt;
            }
        }
        
        if (cnt == 1) {
            cout << 0 << "\n";
            continue;
        }

        vector<int> indeg(cnt, 0), outdeg(cnt, 0);
        int in0 = cnt, out0 = cnt;
        for (int i = 1; i <= n; ++i) {
            for (int j : graph[i]) {
                if (sccId[i] != sccId[j]) {
                    sccGraph[sccId[i]].push_back(sccId[j]);
                    if (!indeg[sccId[j]]) --in0;
                    if (!outdeg[sccId[i]]) --out0;
                    ++indeg[sccId[j]];
                    ++outdeg[sccId[i]];
                }
            }
        }
        
        cout << max(in0, out0) << "\n";
    }
    return 0;
}