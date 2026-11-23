#include <bits/stdc++.h>
#include <cstdio>
using namespace std;

int n, m, ret[10005], visited[10005];
vector<int> graph[10005];
int dfs(int v) {
    visited[v] = 1;
    for (auto& i : graph[v])
        if (!visited[i])
            visited[v] += dfs(i);
    return visited[v];
}
int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; ++i) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[b].push_back(a);
    }
    int maximum = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) visited[j] = 0;
        dfs(i);
        ret[i] = visited[i];
        maximum = max(maximum, ret[i]);
    }
    for (int i = 1; i <= n; ++i)
        if (ret[i] == maximum)
            printf("%d ", i);
    return 0;
}