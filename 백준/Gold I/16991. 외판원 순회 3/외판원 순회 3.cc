#include <bits/stdc++.h>
#include <cstdio>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
const int MAX = 16;
const double INF = 1000000;
int n;
double dist[MAX][MAX], cache[MAX][1 << MAX];
pair<int, int> place[MAX];
double dp(int here, int visited) {
    if (visited == (1 << n) - 1) return dist[here][0];
    double& ret = cache[here][visited];
    if (ret >= 0) return ret;
    ret = INF;
    for (int i = 0; i < n; ++i) {
        if ((visited & (1 << i))) continue;
        double cand = dist[here][i] + dp(i, visited + (1 << i));
        ret = min(ret, cand);
    }
    return ret;
}
int main() {
    memset(cache, -1, sizeof(cache));
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d %d", &place[i].first, &place[i].second);
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i != j) {
                int x = place[i].first - place[j].first, y = place[i].second - place[j].second;
                dist[i][j] = dist[j][i] = sqrt(x * x + y * y);
            }
        }
    }
    printf("%.8f", dp(0, 1));
    return 0;
}