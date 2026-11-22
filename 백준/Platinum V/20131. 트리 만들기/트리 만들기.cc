#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, arr[500500], degree[500500];
int main() {
	fastio;
	cin >> n;
	set<int> leaves;
	vector<pair<int, int>> graph;
	for (int i = 0; i < n - 2; ++i) {
		cin >> arr[i];
		++degree[arr[i]];
	}
	for (int i = 1; i <= n; ++i)
		if (!degree[i]) leaves.insert(i);
	for (int i = 0; i < n - 2; ++i) {
		int a = arr[i], b = *(leaves.rbegin());
		leaves.erase(b);
		if (--degree[a] == 0) leaves.insert(a);
		if (a > b) swap(a, b);
		graph.push_back({ a, b });
	}
	graph.push_back({ *(leaves.begin()), *(leaves.rbegin()) });
	sort(graph.begin(), graph.end());
	for (auto& i : graph) {
		cout << i.first << " " << i.second << endl;
	}
	return 0;
}