#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

struct State {
	int cstate, estate, dist;
};

int n, k, m, arr[12], eq[12], req_color[12], eq_state[1127], visited[1024][1024];
int bfs() {
	visited[0][0] = 1;
	queue<State> q;
	q.push({ req_color[0], 0, 0});
	while (!q.empty()) {
		State v = q.front();
		q.pop();

		//cout << v.cstate << " " << v.estate << " " << v.dist << endl;
		if (v.cstate == (1 << n) - 1 && v.estate == 0) return v.dist;

		for (int i = 0; i < m; ++i) {
			State nv = { v.cstate, v.estate ^ (1 << i), v.dist + 1 };
			if (!visited[nv.cstate][nv.estate]) {
				visited[nv.cstate][nv.estate] = 1;
				q.push(nv);
			}
		}
		for (int i = 0; i < k; ++i) {
			int a = v.cstate, b = eq_state[v.estate], c = req_color[i];
		    State nv = { (b & a) | (~b & c), v.estate, v.dist + 1 };
			if (!visited[nv.cstate][nv.estate]) {
				visited[nv.cstate][nv.estate] = 1;
				q.push(nv);
			}
		}
	}
	return -1;
}
int main() {
	fastio;
	cin >> n >> k >> m;
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	for (int i = 0; i < m; ++i) {
		int t;
		cin >> t;
		for (int j = 0; j < t; ++j) {
			int num; cin >> num; eq[i] += (1 << (num - 1));
		}
	}
	for (int i = 0; i < n; ++i) {
		req_color[arr[i] - 1] += (1 << i);
	}
	for (int i = 0; i < (1 << m); ++i) {
		for (int j = 0; j < m; ++j) {
			if (i & (1 << j)) eq_state[i] |= eq[j];
		}
	}
	cout << bfs();
	return 0;
}