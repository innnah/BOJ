#include<bits/stdc++.h>
using namespace std;

const int mod = 1e9 + 7;

int N, A;

int cc[1010][11][11][11];
int dp(int x, int la, int d, int a) {
    if(x == N) return a == 0;
    int &ret = cc[x][la][d][a];
    if(ret != -1) return ret;

    ret = 0;
    if(d != 10) {
        for(int i = la; i <= 9; i++) {
            if(i == la + d) {
                ret += dp(x + 1, la + d, d, a);
                ret %= mod;
            }
            else if(a) {
                ret += dp(x + 1, i, 10, a - 1);
                ret %= mod;
            }
        }
    }
    else {
        for(int i = la; i <= 9; i++) {
            ret += dp(x + 1, i, i - la, a);
            ret %= mod;
        }
    }
    return ret;
}

int main() {
    cin >> N >> A;

    if(9 < A) {
        cout << 0;
        return 0;
    }

    memset(cc, -1, sizeof(cc));
    int ans = 0;
    for(int i = 1; i <= 9; i++) {
        ans += dp(1, i, 10, A - 1);
        ans %= mod;
    }
    cout << ans;
}