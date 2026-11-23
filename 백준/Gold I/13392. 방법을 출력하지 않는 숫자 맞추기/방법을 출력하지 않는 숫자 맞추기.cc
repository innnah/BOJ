#include <bits/stdc++.h>
#include <cstdio>
using namespace std;

int n, cache[10004][11];
char a[10004], b[10004];
int dp(int idx, int turn) {
    if (idx == n) return 0;
    int& ret = cache[idx][turn];
    if (ret) return ret;
    int turnL = (b[idx] - a[idx] - turn + 20) % 10, turnR = 10 - turnL;
    return ret = min(dp(idx+1, (turn+turnL) % 10) + turnL, dp(idx+1, turn) + turnR);
}
int main() {
    scanf("%d", &n);
    scanf("%s %s", a, b);
    printf("%d", dp(0, 0));
    return 0;
}