#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, sqrtn, arr[100127];
vector<int> buckets[350];
int main() {
	fastio;
	cin >> n;
	sqrtn = sqrt(n);
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
		buckets[i / sqrtn].push_back(arr[i]);
	}
	for (int i = 0; i <= n / sqrtn; ++i) {
		sort(buckets[i].begin(), buckets[i].end());
	}
	int q; cin >> q;
	while (q--) {
		int t; cin >> t;
		if (t == 2) {
			int x, y, z;
			cin >> x >> y >> z;
			x--; y--;
			int cnt = 0;
			int b1 = x / sqrtn, b2 = y / sqrtn;
			for (int i = b1+1; i < b2; ++i) {
				cnt += buckets[i].end() - upper_bound(buckets[i].begin(), buckets[i].end(), z);
			}
			if (b1 == b2) {
				for (int i = x; i <= y; ++i) {
					if (arr[i] > z) cnt++;
				}
			}
			else {
				for (int i = x; i < (b1+1)*sqrtn; ++i) if (arr[i] > z) cnt++;
				for (int i = b2*sqrtn; i <= y; ++i) if (arr[i] > z) cnt++;
			}
			cout << cnt << endl;
		}
		else {
			int x, y;
			cin >> x >> y;
			x--;
			int b = x / sqrtn;
			for (int i = 0; i < buckets[b].size(); ++i) {
				if (buckets[b][i] == arr[x]) {
					buckets[b][i] = y;
					break;
				}
			}
			arr[x] = y;
			sort(buckets[b].begin(), buckets[b].end());
		}
	}
	return 0;
}