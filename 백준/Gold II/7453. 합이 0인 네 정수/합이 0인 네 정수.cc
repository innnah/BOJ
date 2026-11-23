#include <bits/stdc++.h>

using namespace std;

long long n, a[4][4005], s[2][16000003];
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> a[j][i];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            s[0][i*n+j] = a[0][i] + a[1][j];
            s[1][i*n+j] = a[2][i] + a[3][j];
        }
    }
    sort(s[0], s[0]+n*n);
    sort(s[1], s[1]+n*n);
    long long ret = 0;
    for (int i = 0; i < n*n; ++i) {
        ret += (upper_bound(s[1], s[1] + n*n, -s[0][i]) - s[1]) - (lower_bound(s[1], s[1] + n*n, -s[0][i]) - s[1]);
    }
    cout << ret;
    return 0;
}