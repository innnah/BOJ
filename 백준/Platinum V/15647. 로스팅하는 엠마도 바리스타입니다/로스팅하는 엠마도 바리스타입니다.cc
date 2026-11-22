/*
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
메모리 제한 좀 늘려줘요
import sys
input = sys.stdin.readline

def dfs_dp(v):
    visited[v] = 1
    for i, d in tree[v]:
        if not visited[i]:
            dp[i] = dp[v] + (n-nodes[i]*2)*d
            dfs_dp(i)
def dfs(v, dis):
    visited[v] = 1
    distance[v] = dis
    a = 1
    for i, d in tree[v]:
        if not visited[i]:
            a += dfs(i, dis+d)
    nodes[v] = a
    return a    
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
visited = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
nodes = [0 for _ in range(n+1)]
dfs(1, 0)
dp = [0 for _ in range(n+1)]
dp[1] = sum(distance)
visited = [0 for _ in range(n+1)]
dfs_dp(1)
for i in range(1, n+1):
    print(dp[i])
*/
#include <bits/stdc++.h>
#define endl "\n"
using namespace std;
int n, nodes[300500], visited[300500];
long long dist, dp[300500];
vector<pair<int, int>> tree[300500];
void dfs_dp(int v) {
    visited[v] = 1;
    for (auto& i : tree[v]) {
        if (!visited[i.first]) {
            dp[i.first] = dp[v] + (n-nodes[i.first]*2)*i.second;
            dfs_dp(i.first);
        }
    }
}
int dfs(int v, int dis) {
    visited[v] = 1;
    dist += (long long)dis;
    int a = 1;
    for (auto& i : tree[v]) {
        if (!visited[i.first])
            a += dfs(i.first, dis+i.second);
    }
    return nodes[v] = a;
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n;
    for (int i = 0; i < n-1; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        tree[a].push_back({b,c});
        tree[b].push_back({a,c});
    }
    dfs(1, 0);
    dp[1] = dist;
    for (int i = 1; i <= n; ++i) visited[i] = 0;
    dfs_dp(1);
    for (int i = 1; i <= n; ++i) cout << dp[i] << endl;
}