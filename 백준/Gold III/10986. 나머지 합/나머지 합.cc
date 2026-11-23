#include <bits/stdc++.h>
#define endl "\n"
#define ll long long

using namespace std;

int n, m, psum[1000006], cnt[1005];
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        cin >> psum[i];
        psum[i] += psum[i-1];
        psum[i] %= m;
        cnt[psum[i]] += 1;
    }
    ll ret = cnt[0];
    for (int i = 0; i < m; ++i) {
        ret += (ll)cnt[i] * (cnt[i]-1) / 2;
    }
    cout << ret;
    return 0;
}