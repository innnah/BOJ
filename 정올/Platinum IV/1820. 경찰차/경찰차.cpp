#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pll pair<ll, ll>
#define pint pair<int, int>

int n, m;
pair<int, int> coor[1005];
int dp[1005][1005];
int trace[1005][1005];
int distance(int a, int b, int c) {
    pair<int, int> x, y;
    if (a == -1) {
        if (c) x.first = x.second = n;
        else x.first = x.second = 1;
    }
    else {
        x = coor[a];
    }
    y = coor[b];
    return abs(x.first - y.first) + abs(x.second - y.second);
}
int solve(int a, int b) {
    if (max(a, b) == m-1) {
        return 0;
    }
    int& ret = dp[a+1][b+1];
    if (ret != -1) return ret;
    int nxt = max(a, b) + 1;
    int s1 = solve(nxt, b) + distance(a, nxt, 0), s2 = solve(a, nxt) + distance(b, nxt, 1);
    if (s1 <= s2) {
        ret = s1;
        trace[a + 1][b + 1] = 1;
    }
    else {
        ret = s2;
        trace[a + 1][b + 1] = 2;
    }
    return ret;
}
void reconstruct(int a, int b) {
    int nxt = max(a, b) + 1;
    cout << trace[a][b] << endl;
    if (nxt == m) return;
    if (trace[a][b] - 1) {
        reconstruct(a, nxt);
    }
    else {
        reconstruct(nxt, b);
    }
}
int main(void) {
    fastio;
    memset(dp, -1, sizeof(dp));
    cin >> n >> m;
    for (int i = 0; i < m; ++i) {
        cin >> coor[i].first >> coor[i].second;
    }
    cout << solve(-1, -1) << endl;
    reconstruct(0, 0);
    return 0;
}