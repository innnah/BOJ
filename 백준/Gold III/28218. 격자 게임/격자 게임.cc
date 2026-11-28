#include <bits/stdc++.h>

using namespace std;

int n, m, k, arr[351][351], dp[351][351];
inline bool isInside(int x, int y) { return 0<=x && x<m && 0<=y && y<n; }
int dpf(int x, int y) {
    if (x == m-1 && y == n-1) {
        return 0;
    }
    if (dp[y][x] != -1) return dp[y][x];
    int a = 1, b = 1, c = 1;
    if (isInside(x+1, y) && arr[y][x+1]) a = dpf(x+1, y);
    if (isInside(x, y+1) && arr[y+1][x]) b = dpf(x, y+1);
    for (int i = 1; i <= k; ++i) {
        if (isInside(x+i, y+i) && arr[y+i][x+i]) c = c & dpf(x+i, y+i);
    }
    if (a == 0 || b == 0 || c == 0) return dp[y][x] = 1;
    return dp[y][x] = 0;
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n >> m >> k;
    for (int i = 0; i < n; ++i) {
        string a;
        cin >> a;
        for (int j = 0; j < m; ++j)
            arr[i][j] = (a[j] == '.');
    }
    memset(dp, -1, sizeof(dp));
    int q;
    cin >> q;
    while (q--) {
        int x, y;
        cin >> y >> x;
        --y; --x;
        int ret = dpf(x, y);
        if (ret) cout << "First" << "\n";
        else cout << "Second" << "\n";
    }
    return 0;
}