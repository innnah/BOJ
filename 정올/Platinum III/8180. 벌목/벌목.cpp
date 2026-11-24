#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<int> arr(n);
        for (auto& x : arr) cin >> x;
        sort(arr.begin(), arr.end());
        vector<tuple<int, int, int, int>> event;
        for (int x : arr) event.push_back({x, 0, 0, 0});
        for (int j = 0; j < m; j++) {
            int a, b, c;
            cin >> a >> b >> c;
            int exist = (upper_bound(arr.begin(), arr.end(), b) - arr.begin())
                      - (lower_bound(arr.begin(), arr.end(), a) - arr.begin());
            event.push_back({a, -1, b, exist - c});
        }
        sort(event.begin(), event.end());
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        int ans = 0;
        for (auto& [l, i, r, t] : event) {
            if (i == -1) {
                pq.push({ans + t, r});
            } else {
                while (!pq.empty() && pq.top().second < l) pq.pop();
                if (pq.empty() || pq.top().first > ans) ans++;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}