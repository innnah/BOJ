#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int a, b, n;
pair<int, int> arr1[500127], arr2[500127];
int main() {
	fastio;
	cin >> a >> b >> n;
	for (int i = 0; i < n; ++i) {
		int t1, t2; cin >> t1 >> t2;
		arr1[i] = { t1, i };
		arr2[i] = { t2, i };
	}
	if (b > a) {
		cout << "-1 -1";
		return 0;
	}
	int t = a - b + 1;
	int m = 987654321;
	pair<int, int> ans = { -1, -1 };
	for (int i = 0; i < n; ++i) {
		int v1 = arr1[i].first, v2 = arr2[i].first;
		if (t <= v1 && v1 <= m) {
			m = v1;
			ans = { i + 1, -1 };
		}
		if (t <= v2 && v2 <= m) {
			m = v2;
			ans = { -1, i + 1 };
		}
	}
	sort(arr1, arr1 + n);
	for (int i = 0; i < n; ++i) {
		auto idx = lower_bound(arr1, arr1 + n, make_pair(t - arr2[i].first, -1));
		if (idx == arr1 + n) continue;
		if (idx->second == i) idx++;
		if (idx == arr1 + n) continue;
		int v = arr2[i].first + idx->first;
		if (t <= v && v <= m) {
			m = v;
			ans = { idx->second + 1, arr2[i].second + 1 };
		}
	}
	if (ans == make_pair(-1, -1)) {
		cout << "No";
	}
	else {
		cout << ans.first << " " << ans.second;
	}
	return 0;
}