#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, cnt, state[100127], visited[200127], sccId[200127];
vector<int> p[100127], graph[200127], rgraph[200127], s;
void kosa(int v) {
	visited[v] = 1;
	for (auto& i : graph[v]) {
		if (!visited[i]) kosa(i);
	}
	s.push_back(v);
}
void raju(int v) {
	visited[v] = 1;
	sccId[v] = cnt;
	for (auto& i : rgraph[v]) {
		if (!visited[i]) raju(i);
	}
}
int main() {
	fastio;
	cin >> n >> m;
	for (int i = 0; i < n; ++i) cin >> state[i];
	for (int i = 0; i < m; ++i) {
		int s;
		cin >> s;
		for (int j = 0; j < s; ++j) {
			int a;
			cin >> a;
			--a;
			p[a].push_back(i);
		}
	}
	for (int i = 0; i < n; ++i) {
		graph[p[i][0]].push_back((!state[i]) * m + p[i][1]);
		graph[p[i][1]].push_back((!state[i]) * m + p[i][0]);
		graph[m + p[i][0]].push_back(state[i] * m + p[i][1]);
		graph[m + p[i][1]].push_back(state[i] * m + p[i][0]);
	}
	for (int i = 0; i < 2 * m; ++i) {
		for (auto& j : graph[i]) {
			rgraph[j].push_back(i);
		}
	}

	for (int i = 0; i < 2 * m; ++i) {
		if (!visited[i]) kosa(i);
	}
	memset(visited, 0, sizeof(visited));
	while (!s.empty()) {
		int v = *s.rbegin();
		s.pop_back();
		if (!visited[v]) {
			raju(v);
			++cnt;
		}
	}
	for (int i = 0; i < m; ++i) {
		if (sccId[i] == sccId[i + m]) {
			cout << 0;
			return 0;
		}
	}
	cout << 1;
	return 0;
}