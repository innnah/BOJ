#include <bits/stdc++.h>

using namespace std;
#define ll long long

int n;
ll cache[105][10][1<<11];
const int MOD = 1000000000;
ll dp(int where, int num, int used) {
    if (where == n) {
        return used == (1 << 10) - 1;
    }
    ll& ret = cache[where][num][used];
    if (ret != -1) return ret;
    ret = 0;
    if (num != 0) 
        ret = (ret + dp(where+1, num-1, used | (1 << num-1))) % MOD;
    if (num != 9)
        ret = (ret + dp(where+1, num+1, used | (1 << num+1))) % MOD;
    return ret;
}
int main() {
    memset(cache, -1, sizeof(cache));
    cin >> n;
    ll ret = 0;
    for (int i = 1; i < 10; ++i) {
        ret += dp(1, i, 1 << i);
        ret %= MOD;
    }
    cout << ret;
    return 0;
}