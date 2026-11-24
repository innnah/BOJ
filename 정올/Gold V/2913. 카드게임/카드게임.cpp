#include <bits/stdc++.h>

using namespace std;

int n, cache[2023][2023], a[2023], b[2023]; // Happy New Year!!
int dp(int idxA, int idxB) {
    if (idxA == n || idxB == n) return 0;
    int& ret = cache[idxA][idxB];
    if (ret != -1) return ret;
    ret = 0;
    ret = max(ret, dp(idxA+1, idxB+1));
    ret = max(ret, dp(idxA+1, idxB));
    if (a[idxA] > b[idxB]) ret = max(ret, dp(idxA, idxB+1) + b[idxB]);
    return ret;
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    memset(cache, -1, sizeof(cache));
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    for (int i = 0; i < n; ++i)
        cin >> b[i];
    cout << dp(0, 0);
    return 0;
}