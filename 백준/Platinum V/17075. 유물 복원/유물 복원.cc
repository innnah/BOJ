#include <bits/stdc++.h>
using namespace std;

int n, m, k, arr[51][51], dp[2501][2501], trace[2501][2501];
int dpf(int rc, int mp) {
    if (rc == n*m) return mp == 0;
    int& ret = dp[rc][mp];
    if (ret != -1) return ret;
    
    int r = rc/m, c = rc-r*m;
    int mul = (r+1)*(c+1)*(n-r)*(m-c);
    if (arr[r][c] != -1) return ret = dpf(rc+1, (mp+arr[r][c]*mul)%k);
    int r1 = dpf(rc+1, (mp+mul)%k), r0 = dpf(rc+1, mp);
    ret = r0 | r1;
    if (r0) trace[rc][mp] = mp;
    if (r1) trace[rc][mp] = (mp+mul)%k;
    return ret;
}
void reconstruct(int rc, int mp) {
    if (rc == n*m) return;
    int r = rc/m, c = rc-r*m;
    int mul = (r+1)*(c+1)*(n-r)*(m-c);
    if (arr[r][c] != -1) {
        reconstruct(rc+1, (mp+arr[r][c]*mul)%k);
        return;
    }
    arr[r][c] = (trace[rc][mp] != mp);
    reconstruct(rc+1, trace[rc][mp]);
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    cin >> n >> m >> k;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> arr[i][j];
        }
    }
    memset(dp, -1, sizeof(dp));
    int ret = dpf(0, 0);
    cout << ret*2-1 << endl;
    if (ret) {
        reconstruct(0, 0);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cout << arr[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}