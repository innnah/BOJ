#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const ll INF = 987654321234567;
int main() {
    fastio;
	vector<pair<int, pair<int, int>>> events;
	for (int i = 0; i < 2; ++i) {
		int n;
		cin >> n;
		while (n--) {
			int cores, freq, price;
			cin >> cores >> freq >> price;
			if (i == 0) price *= -1;
			else cores *= -1;
			events.push_back({ freq, {cores, price} });
		}
	}
	sort(events.rbegin(), events.rend());
	vector<ll> dp = { 0 };
	for (int i = 0; i < events.size(); ++i) {
		vector<ll> dp2 = dp;
		for (int j = 0; j < dp.size(); ++j) {
			int idx = j + events[i].second.first;
			if (idx >= 0) {
				ll cost = dp[j] + events[i].second.second;
				while (dp2.size() <= idx) dp2.push_back(-INF);
				dp2[idx] = max(dp2[idx], cost);
			}
		}
		dp = dp2;
	}
	ll ans = 0;
	for (auto& i : dp) ans = max(ans, i);
	cout << ans;
    return 0;
}