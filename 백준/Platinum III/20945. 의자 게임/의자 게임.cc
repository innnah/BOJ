#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, k, arr[100100];
bool f(int x) {
	map<int, int> d;
	for (int i = 0; i < k - x; ++i) {
		if (d.find(arr[i]) == d.end()) d[arr[i]] = 0;
		++d[arr[i]];
	}
	for (int i = 0; i < n; ++i) {
		int idx = (i + k - x) % n;
		if (d.size() == k - x && d.rbegin()->first - d.begin()->first < k) return true;
		--d[arr[i]];
		if (d[arr[i]] == 0) d.erase(arr[i]);
		if (d.find(arr[idx]) == d.end()) d[arr[idx]] = 0;
		++d[arr[idx]];
	}
	return false;
}
int main() {
	fastio;
	cin >> n >> k;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	int lo = 0, hi = k;
	while (lo < hi) {
		int mid = (lo + hi) / 2;
		if (f(mid)) hi = mid;
		else lo = mid + 1;
	}
	cout << lo;
	return 0;
}