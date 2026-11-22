#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;
long long n, a[100010], b[100010], visited[100010];
vector<pair<int, long long>> tree[100010];
long long dfs(int v) {
    visited[v] = 1;
    long long s = 0;
    for (auto& i : tree[v]) {
        if (!visited[i.first]) {
            s += dfs(i.first) * i.second;
            s %= MOD;
            s += i.second;
            s %= MOD;
            long long tmp = (a[i.first]+1)*i.second;
            tmp %= MOD;
            b[v] += (s-tmp+MOD)*tmp;
            b[v] %= MOD;
        }
    }
    a[v] = s;
    return a[v];
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int n;
    cin >> n;
    for (int i = 0; i < n-1; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        tree[a].push_back({b,c});
        tree[b].push_back({a,c});
    }
    dfs(1);
    long long ret = 0;
    for (int i = 1; i <= n; ++i) {
        ret += a[i] + b[i];
        ret %= MOD;
    }
    cout << ret;
    return 0;
}