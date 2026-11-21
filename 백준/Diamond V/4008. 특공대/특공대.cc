#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);

struct Line {
    ll a;
    ll b;
    double s;
};
double intersect(const Line& l1, const Line& l2) {
    return (double)(l2.b - l1.b) / (l1.a - l2.a);
}
ll n, a, b, c, arr[1000100], p[1000100], dp[1000100];
Line lines[1000100];
int main() {
    fastio;
    cin >> n >> a >> b >> c;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    p[0] = arr[0];
    for (int i = 1; i < n; ++i) {
        p[i] = p[i - 1] + arr[i];
    }
    int add = 0;
    dp[0] = a * p[0] * p[0] + b * p[0] + c;
    lines[add++] = {p[0], a*p[0]*p[0]-b*p[0]+dp[0], -1024.0};
    for (int i = 1; i < n; ++i) {
        ll x = -2 * a * p[i];
        int fpos = add - 1;
        if (x < lines[add - 1].s) {
            int lo = 0, hi = add - 1;
            while (lo + 1 < hi) {
                int mid = (lo + hi) / 2;
                if (x < lines[mid].s) {
                    hi = mid - 1;
                }
                else {
                    lo = mid;
                }
            }
            if (x >= lines[hi].s) fpos = hi;
            else fpos = lo;
        }
        dp[i] = max(lines[fpos].a * x + lines[fpos].b, 0LL) + a * p[i] * p[i] + b * p[i] + c;
        Line g = { p[i], a * p[i] * p[i] - b * p[i] + dp[i], -1024.0 };
        while (add > 0) {
            g.s = intersect(g, lines[add - 1]);
            if (g.s > lines[add - 1].s) break;
            --add;
        }
        lines[add++] = g;
    }
    cout << dp[n - 1];
    return 0;
}