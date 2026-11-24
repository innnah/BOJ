#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ll n;
    int m;
    cin >> n >> m;
    vector<tuple<ll, ll, int>> lines;
    vector<int> deleted(m, 0);
    for (int i = 0; i < m; i++) {
        ll a, b;
        cin >> a >> b;
        if (b < a) {
            lines.push_back({a, b + n, i});
        } else {
            lines.push_back({a, b, i});
            lines.push_back({a + n, b + n, i});
        }
    }
    sort(lines.begin(), lines.end(), [](const tuple<ll, ll, int>& x, const tuple<ll, ll, int>& y) {
        if (get<0>(x) != get<0>(y)) return get<0>(x) < get<0>(y);
        if (get<1>(x) != get<1>(y)) return get<1>(x) > get<1>(y);
        return get<2>(x) < get<2>(y);
    });
    ll start = get<0>(lines[0]), end = get<1>(lines[0]);
    for (size_t i = 1; i < lines.size(); i++) {
        ll l = get<0>(lines[i]), r = get<1>(lines[i]);
        if (start <= l && l <= r && r <= end) {
            deleted[get<2>(lines[i])] = 1;
        } else {
            start = l;
            end = r;
        }
    }
    for (int i = 0; i < m; i++) {
        if (!deleted[i]) cout << i + 1 << ' ';
    }
    return 0;
}