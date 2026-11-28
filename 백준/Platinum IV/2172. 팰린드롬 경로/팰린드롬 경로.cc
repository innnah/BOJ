#include <bits/stdc++.h>
using namespace std;
int n, l, arr[21][21], dp[21][21][21][21][21], dx[8] = {0, 0, -1, 1, -1, 1, -1, 1}, dy[8] = {1, -1, 0, 0, 1, 1, -1, -1};
inline bool isInside(int x, int y) { return 0<=x&&x<n&&0<=y&&y<n; }
int dpf(int idx, int x1, int y1, int x2, int y2) {
    if (idx <= 0) return 1;
    int& ret = dp[idx][x1][y1][x2][y2];
    if (ret != -1) return ret;
    ret = 0;
    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 8; ++j) {
            int nx1 = x1 + dx[i], ny1 = y1 + dy[i], nx2 = x2 + dx[j], ny2 = y2 + dy[j];
            if (isInside(nx1, ny1) && isInside(nx2, ny2) && arr[ny1][nx1] == arr[ny2][nx2])
                ret += dpf(idx-1, nx1, ny1, nx2, ny2);
        }
    }
    return ret;
}
int main() {
    memset(dp, -1, sizeof(dp));
    cin >> n >> l;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> arr[i][j];
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (l%2) ret += dpf(l/2, j, i, j, i);
            else {
                for (int k = 0; k < 8; ++k) {
                    int oi = i + dy[k], oj = j + dx[k];
                    if (isInside(oj, oi) && arr[i][j] == arr[oi][oj])
                        ret += dpf(l/2-1, j, i, oj, oi);
                }
            }
        }
    }
    cout << ret;
    return 0;
}