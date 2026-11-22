#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

vector<int> arr;
vector<int> button[9] = { {0, 1, 3, 4}, {0, 1, 2}, {1, 2, 4, 5}, {0, 3, 6}, {1, 3, 4, 5, 7}, {2, 5, 8}, {3, 4, 6, 7}, {6, 7, 8}, {4, 5, 7, 8} };
vector<int> ans;
void solve(int idx, vector<int> state, vector<int> clicked) {
	if (idx == 9) {
		bool flag = 1;
		for (int i = 0; i < 9; ++i) {
			flag = flag & (!state[i]);
		}
		if (flag && ans.size() > clicked.size()) {
			ans = clicked;
		}
		return;
	}
	for (int i = 0; i <= 3; ++i) {
		solve(idx + 1, state, clicked);
		for (int j = 0; j < button[idx].size(); ++j) {
			state[button[idx][j]] = (state[button[idx][j]] + 1) % 4;
		}
		clicked.push_back(idx + 1);
	}
	for (int i = 0; i <= 3; ++i) {
		for (int j = 0; j < button[idx].size(); ++j) {
			state[button[idx][j]] = (state[button[idx][j]] + 3) % 4;
		}
		clicked.pop_back();
	}
}
int main() {
	fastio;
	arr.resize(9);
	ans.resize(100);
	for (int i = 0; i < 3; ++i)
		for (int j = 0; j < 3; ++j)
			cin >> arr[i * 3 + j];
	solve(0, arr, {});
	for (int i = 0; i < ans.size(); ++i) {
		cout << ans[i] << " ";
	}
	return 0;
}