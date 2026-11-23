#include <bits/stdc++.h>
#define Node pair<pair<int, int>, int>

using namespace std;

int n, c, m[60][60], dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
int canGo[4][6] = {{0, 1, 0, 1, 0, 1},
                   {1, 0, 1, 0, 0, 1},
                   {0, 0, 1, 1, 1, 0},
                   {1, 1, 0, 0, 1, 0}};
int opposite[4] = {1, 0, 3, 2};
bool visited[60][60];
inline bool isInside(int x, int y) { return 0<=x&&x<n&&0<=y&&y<n; }
int bfs() {
    queue<Node> q;
    q.push({{0, 0}, 1});
    visited[0][0] = 1;
    if (!(m[0][0] == 1 || m[0][0] == 3 || m[0][0] == 5)) return -1;
    while (!q.empty()) {
        Node v = q.front();
        int x = v.first.first, y = v.first.second, dist = v.second;
        if (x == n-1 && y == n-1 && canGo[1][m[y][x]]) return dist;
        q.pop();
        for (int i = 0; i < 4; ++i) {
            if (canGo[i][m[y][x]]) {
                int nx = x + dx[i], ny = y + dy[i];
                if (isInside(nx, ny) && !visited[ny][nx] && canGo[opposite[i]][m[ny][nx]]) {
                    visited[ny][nx] = 1;
                    q.push({{nx, ny}, dist+1});
                }
            }
        }
    }
    return -1;
}
int main() {
    cin >> n >> c;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> m[i][j];
    if (c==0)
        cout << bfs();
    else {
        int ret = 987654321;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int tmp = m[i][j];
                for (int k = 0; k < 6; ++k) {
                    if (k == tmp) continue;
                    for (int a = 0; a < n; ++a)
                        for (int b = 0; b < n; ++b)
                            visited[a][b] = 0;
                    m[i][j] = k;
                    int cand = bfs();
                    if (cand != -1) ret = min(ret, cand);
                    m[i][j] = tmp;
                }
            }
        }
        if (ret != 987654321) cout << ret;
        else cout << -1;
    }
    return 0;
}