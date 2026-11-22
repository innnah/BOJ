#include <bits/stdc++.h>
using namespace std;
int n;
vector<pair<int, int>> colors[100127];
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        colors[b].push_back(make_pair(a, b));
    }
    long long ans = 0L;
    for (int i = 1; i <= n; ++i) {
        sort(colors[i].begin(), colors[i].end());
        for (int j = 0; j < colors[i].size(); ++j) {
            if (j == 0) {
                ans += colors[i][j+1].first - colors[i][j].first;
            }
            else if (j == colors[i].size()-1) {
                ans += colors[i][j].first - colors[i][j-1].first;
            }
            else {
                ans += min(colors[i][j+1].first - colors[i][j].first, colors[i][j].first - colors[i][j-1].first);
            }
        }
    }
    cout << ans;
    return 0;
}