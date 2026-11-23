#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

const int MAX = 16;
int n;
int cache[MAX][1 << MAX];
string words[MAX];
int dp(int here, int visited) {
    if (visited == (1 << n) - 1) return 0;
    int& ret = cache[here][visited];
    if (ret >= 0) return ret;
    ret = 0;
    int size = words[here].size();
    for (int i = 0; i < n; ++i) {
        if ((visited & (1 << i)) || words[here][size-1] != words[i][0]) continue;
        int cand = words[i].size() + dp(i, visited + (1 << i));
        ret = max(ret, cand);
    }
    return ret;
}
int main() {
    fastio;
    memset(cache, -1, sizeof(cache));
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> words[i];
    }
    int ret = 0;
    for (int i = 0; i < n; ++i) {
        ret = max(ret, (int)(dp(i, (1 << i)) + words[i].size()));
    }
    cout << ret;
    return 0;
}