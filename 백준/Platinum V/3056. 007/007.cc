#include <bits/stdc++.h>
#include <cstdio>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

const int MAX = 20;
int n, rate[MAX][MAX];
double cache[1 << MAX];
double dp(int here, int visited) {
    if (here == n) return 1;
    double& ret = cache[visited];
    if (ret >= 0) return ret;
    ret = 0;
    for (int i = 0; i < n; ++i) {
        if (visited & (1 << i)) continue;
        ret = max(ret, rate[here][i] * dp(here + 1, visited + (1 << i)) / 100);
    }
    return ret;
}
int main() {
    memset(cache, -1, sizeof(cache));
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            scanf("%d", &rate[i][j]);
    printf("%lf", dp(0, 0) * 100);
    return 0;
}