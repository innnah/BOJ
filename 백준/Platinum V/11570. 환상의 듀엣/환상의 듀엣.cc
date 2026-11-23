#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, song[2005], dp[2005][2005];
inline int hard(int a, int b) { 
    if (a == -1) return 0;
    return abs(song[a] - song[b]); 
}
int sing(int a, int b) {
    int nxt = max(a, b) + 1;
    if (nxt == n) return 0;
    int& ret = dp[a + 1][b + 1];
    if (ret != -1) return ret;
    return ret = min(sing(nxt, b) + hard(a, nxt), sing(a, nxt) + hard(b, nxt));
}
int main(void) {
    fastio;
    memset(dp, -1, sizeof(dp));
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> song[i];
    }
    cout << sing(-1, -1);
    return 0;
}