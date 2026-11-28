#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

ll n, l, c[1001000][2];
vector<ll> arr[1001000];
bool compare(vector<ll>& a, vector<ll>& b) {
	return a[0]+b[1] > a[1]+b[0];
}
int main() {
	fastio;
	cin >> n >> l;
	for (int i = 0; i < n; ++i) {
		cin >> c[i][0] >> c[i][1];
		arr[i] = vector<ll>(3);
		arr[i][0] = c[i][0] * c[i][1], arr[i][1] = max(c[i][0] * (c[i][1] - 5), 0LL), arr[i][2] = c[i][1];
	}
	sort(arr, arr + n, compare);
	int c = 0;
	ll t = 0;
	for (int i = 0; i < n; ++i) {
		ll tmp = max(0LL, c - l + arr[i][0]);
		c -= tmp;
		t += tmp;
		c += arr[i][1];
		t += arr[i][2];
	}
	cout << t << endl;
	return 0;
}