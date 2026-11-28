#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAX = 10100;
int n, m, group[MAX], g_cnt;
int visited[MAX], ft_arr[MAX], ft_cnt, in_edge[MAX];
vector<int> graph[MAX], rgraph[MAX], scc_arr[MAX], scc_graph[MAX];
void kosa(int v) {
    visited[v] = 1;
    for (auto& i : graph[v])
        if (!visited[i])
            kosa(i);
    ft_arr[++ft_cnt] = v;
}
void raju(int v) {
    group[v] = g_cnt;
    scc_arr[g_cnt].push_back(v);
    for (auto& i : rgraph[v])
        if (!group[i])
            raju(i);
}
void dfs(int v) {
    visited[v] = 1;
    for (auto& i : scc_graph[v]) {
        if (!visited[i])
            dfs(i);
    }
}
int main() {
    fastio;
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        rgraph[b].push_back(a);
    }
    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) kosa(i);
    }
    for (int i = ft_cnt; i > 0; --i) {
        int s = ft_arr[i];
        if (!group[s]) {
            ++g_cnt;
            raju(s);
        }
    }
    for (int i = 1; i <= n; ++i) {
        for (auto& j : graph[i]) {
			if (group[j] != group[i]) {
				scc_graph[group[j]].push_back(group[i]);
				in_edge[group[i]] = 1;
			}
        }
    }
    for (int i = 1; i <= g_cnt; ++i) {
        visited[i] = 0;
    }
    for (int i = 1; i <= g_cnt; ++i) {
        if (!in_edge[i]) {
            dfs(i);
            bool flag = true;
            for (int j = 1; j <= g_cnt; ++j) {
                if (!visited[j]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                cout << scc_arr[i].size();
            }
            else {
                cout << 0;
            }
            break;
        }
    }
    return 0;
}