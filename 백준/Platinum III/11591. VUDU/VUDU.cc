#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

ll n, arr[1000127], q;
ll arr2[1000127];
ll merge(int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;
	ll ans = 0;
	while (i <= mid && j <= right) {
		if (arr[i] <= arr[j]) {
			arr2[k++] = arr[i++];
		}
		else {
			ans += (ll)(i - left);
			arr2[k++] = arr[j++];
		}
	}
	if (i <= mid)
		while (i <= mid) arr2[k++] = arr[i++];
	else
		while (k <= right) { ans += (ll)(i - left); arr2[k++] = arr[j++]; }

	for (int x = left; x <= right; ++x) arr[x] = arr2[x];
	return ans;
}
ll merge_sort(int left, int right) {
	if (left >= right) return 0LL;
	int mid = (left + right) / 2;
	ll ans1 = merge_sort(left, mid);
	ll ans2 = merge_sort(mid + 1, right);
	ll ans3 = merge(left, mid, right);
	return ans1 + ans2 + ans3;
}
int main() {
	fastio;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		cin >> arr[i];
	}
	cin >> q;
	for (int i = 1; i <= n; ++i) {
		arr[i] -= q;
	}
	for (int i = 1; i <= n; ++i) {
		arr[i] += arr[i - 1];
	}
	cout << merge_sort(0, n) << endl;
	return 0;
}