#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#include <cstdio>

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long long int ulli;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

int n, m, s, t;
bitset<100001> elevator[105];
vector<int> graph[105];
struct Info {
	int v;
	int dist;
	vector<int> path;
};
pair<int, vector<int>> bfs(int start) {
	queue<Info> q;
	vector<int> visited(n, 0);
	visited[start] = 1;
	q.push({ start, 1, { start } });
	while (!q.empty()) {
		Info v = q.front();
		q.pop();
		if (elevator[v.v][t]) return { v.dist, v.path };
		for (auto& i : graph[v.v]) {
			if (!visited[i]) {
				v.path.push_back(i);
				q.push({ i, v.dist + 1, v.path });
				v.path.pop_back();
				visited[i] = 1;
			}
		}
	}
	return  { 987654321, {} };
}
int main() {
	fastio;
	cin >> n >> m;
	for (int i = 0; i < m; ++i) {
		int a, b;
		cin >> a >> b;
		for (int j = a; j <= n; j += b) {
			elevator[i].set(j, true);
		}
	}
	cin >> s >> t;
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < m; ++j) {
			if ((elevator[i] & elevator[j]) != 0) {
				graph[i].push_back(j);
			}
		}
	}
	int mini = 987654321;
	vector<int> minPath;
	for (int i = 0; i < m; ++i) {
		if (elevator[i].test(s) == 1) {
			pair<int, vector<int>> cand = bfs(i);
			if (mini > cand.first) {
				mini = cand.first;
				minPath = cand.second;
			}
		}
	}
	if (mini == 987654321) {
		cout << -1 << endl;
		return 0;
	}
	cout << mini << endl;
	for (auto& i : minPath) {
		cout << i+1 << endl;
	}
	return 0;
}