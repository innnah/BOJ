#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

struct State {
	int w;
	double p;
	int d;
	bool operator< (const State& x) {
		return p < x.p;
	}
};

int n, l;
State arr[50127];
int main() {
	fastio;
	cin >> n >> l;
	int sum_weight = 0, lef = 0;
	multiset<pair<int, int>> ms;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i].w >> arr[i].p >> arr[i].d;
		sum_weight += arr[i].w;
		if (arr[i].d == -1) ++lef;
	}
	sort(arr, arr + n);

	int a = 0, b = 0;
	for (int i = 0; i < n; ++i) {
		if (arr[i].d == -1) {
			ms.insert({ arr[i].p, a++ });
		}
		else {
			ms.insert({ l - arr[i].p, lef + b++});
		}
	}

	int weight = 0, t = 0;
	while (weight * 2 < sum_weight) {
		pair<int, int> val = *ms.begin();
		weight += arr[val.second].w;
		t = val.first;
		ms.erase(ms.begin());
	}
	
	queue<int> q;
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		if (arr[i].d == -1) {
			while (q.size() && q.front() + 2 * t < arr[i].p) q.pop();
			ret += q.size();
		}
		else q.push(arr[i].p);
	}
	cout << ret << endl;
	return 0;
}