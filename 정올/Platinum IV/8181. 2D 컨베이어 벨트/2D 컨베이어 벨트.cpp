#include <bits/stdc++.h>
using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
map<char, int> d = {{'L', 0}, {'R', 1}, {'U', 2}, {'D', 3}, {'-', -1}};
char rd[4] = {'R', 'L', 'D', 'U'};

int n, m;
vector<string> board;
vector<vector<int>> usable;
int newans;

bool isInside(int x, int y) { return 0 <= x && x < n && 0 <= y && y < n; }
bool nxt(int x, int y, char dir) {
    return isInside(x, y) && !usable[x][y] && (board[x][y] == '-' || board[x][y] == dir);
}

void dfs(int x, int y) {
    if (usable[x][y]) return;
    usable[x][y] = 1;
    newans -= 1;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (isInside(nx, ny) && !usable[nx][ny] &&
            (board[nx][ny] == '-' || d[rd[d[board[nx][ny]]]] == i)) {
            dfs(nx, ny);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    vector<tuple<int, int, char>> querys;
    for (int i = 0; i < m; i++) {
        int a, b;
        string c;
        cin >> a >> b >> c;
        querys.push_back({a - 1, b - 1, c[0]});
    }

    board.assign(n, string(n, '-'));
    for (auto& [x, y, dir] : querys) board[x][y] = dir;

    usable.assign(n, vector<int>(n, 0));
    newans = n * n;
    for (int i = 0; i < n; i++) {
        if (nxt(0, i, 'U')) dfs(0, i);
        if (nxt(n - 1, i, 'D')) dfs(n - 1, i);
        if (nxt(i, 0, 'L')) dfs(i, 0);
        if (nxt(i, n - 1, 'R')) dfs(i, n - 1);
    }

    vector<int> ans(m, 0);
    ans[m - 1] = newans;
    for (int i = m - 2; i >= 0; i--) {
        auto [x, y, dir] = querys[i + 1];
        newans = ans[i + 1];
        board[x][y] = '-';
        for (int j = 0; j < 4; j++) {
            int nx = x + dx[j], ny = y + dy[j];
            if (!isInside(nx, ny) || usable[nx][ny]) {
                dfs(x, y);
                break;
            }
        }
        ans[i] = newans;
    }
    for (int i = 0; i < m; i++) cout << ans[i] << '\n';
    return 0;
}