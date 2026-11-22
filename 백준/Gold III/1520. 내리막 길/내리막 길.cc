/*
import sys
sys.setrecursionlimit(250250)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def isInside(x, y): return 0 <= x < m and 0 <= y < n
def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if dp[y][x] != -1: return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if isInside(nx, ny) and l[ny][nx] < l[y][x]:
            dp[y][x] += dfs(nx, ny)
    return dp[y][x]
*/
#include <bits/stdc++.h>
using namespace std;
int n, m, arr[501][501], dp[501][501], dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
bool isInside(int x, int y) {
    return (0 <= x && x < m && 0 <= y && y < n);
}
int dfs(int x, int y) {
    if (x == m-1 && y == n-1) return 1;
    int& ret = dp[y][x];
    if (ret != -1) return ret;
    ret = 0;
    for (int i = 0; i < 4; ++i) {
        int nx = x + dx[i], ny = y + dy[i];
        if (isInside(nx, ny) && arr[ny][nx] < arr[y][x]) ret += dfs(nx, ny);
    }
    return ret;
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    memset(dp, -1, sizeof(dp));
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            cin >> arr[i][j];
    cout << dfs(0, 0);
    return 0;
}