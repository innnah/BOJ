#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>
#include <random>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt
#define pll pair<ll, ll>
#define pint pair<int, int>

int n, m, arr[10][10], visited[10][10];
int dx[4] = { 0, 0, -1, 1 }, dy[4] = { -1, 1, 0, 0 };
bool isInside(int x, int y) { return 0 <= x && x < m && 0 <= y && y < n; }
int bfs() {
    queue<pair<int, int>> q;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (arr[i][j] == 2) {
                q.push({ j, i });
                visited[i][j] = 1;
            }
        }
    }
    while (!q.empty()) {
        pair<int, int> v = q.front();
        q.pop();
        int x = v.first, y = v.second;
        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i], ny = y + dy[i];
            if (isInside(nx, ny) && arr[ny][nx] == 0 && !visited[ny][nx]) {
                visited[ny][nx] = 1;
                q.push({ nx, ny });
            }
        }
    }
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (!visited[i][j] && arr[i][j] == 0) ret += 1;
        }
    }
    return ret;
}
int main() {
    fastio;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> arr[i][j];
        }
    }
    int ret = 0;
    for (int c1 = 0; c1 < n * m; ++c1) {
        for (int c2 = c1 + 1; c2 < n * m; ++c2) {
            for (int c3 = c2 + 1; c3 < n * m; ++c3) {
                int x1 = c1 % m, x2 = c2 % m, x3 = c3 % m;
                int y1 = c1 / m, y2 = c2 / m, y3 = c3 / m;
                //cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << " " << arr[y1][x1] << " " << arr[y2][x2] << " " << arr[y3][x3] << endl;
                if (arr[y1][x1] == 0 && arr[y2][x2] == 0 && arr[y3][x3] == 0) {
                    arr[y1][x1] = arr[y2][x2] = arr[y3][x3] = 1;
                    for (int i = 0; i < n; ++i) {
                        for (int j = 0; j < m; ++j) {
                            visited[i][j] = 0;
                        }
                    }
                    int cand = bfs();
                    ret = max(ret, cand);
                    arr[y1][x1] = arr[y2][x2] = arr[y3][x3] = 0;
                }
            }
        }
    }
    cout << ret << endl;
    return 0;
}