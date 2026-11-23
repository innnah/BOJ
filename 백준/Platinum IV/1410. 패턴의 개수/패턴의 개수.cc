#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

typedef int cache_type;
const int MAX = 15;
const int INF = 987654321;
int n, k;
string patterns[MAX];
cache_type cache[55][1 << MAX];
cache_type dp(int here, int visited) {
    if (here == patterns[0].size()) {
        return __builtin_popcount(visited) == k;
    }
    cache_type& ret = cache[here][visited];
    if (ret >= 0) return ret;
    ret = 0;
    for (char i = 'a'; i <= 'z'; ++i) {
        int v = 0;
        for (int j = 0; j < n; ++j) {
            if ((patterns[j][here] == i || patterns[j][here] == '?') && (visited & (1 << j))) {
                v |= (1 << j);
            }
        }
        ret += dp(here + 1, v);
        ret %= 1000003;
    }
    return ret;
}
int main() {
    fastio;
    memset(cache, -1, sizeof(cache));
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> patterns[i];
    }
    cout << dp(0, (1 << n) - 1) % 1000003;
    return 0;
}