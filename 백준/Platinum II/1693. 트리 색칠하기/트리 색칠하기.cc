#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>
#include <random>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt
#define pll pair<ll, ll>
#define pint pair<int, int>

int n, dp[100010][17];
vector<int> graph[100010];
int dpf(int v, int c, int p) {
    if (dp[v][c] != -1) return dp[v][c];
    dp[v][c] = 0;
    for (auto& i : graph[v]) {
        if (i != p) {
            int sub = 987654321;
            for (int j = 0; j < 17; ++j) {
                if (c != j) {
                    sub = min(dpf(i, j, v) + j + 1, sub);
                }
            }
            if (sub == 987654321) return 987654321;
            dp[v][c] += sub;
        }
    }
    return dp[v][c];
}
int main() {
    fastio;
    cin >> n;
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    memset(dp, -1, sizeof(dp));
    int ret = 987654321;
    for (int i = 0; i < 17; ++i) {
        ret = min(ret, dpf(1, i, 0) + i + 1);
    }
    cout << ret;
    return 0;
}