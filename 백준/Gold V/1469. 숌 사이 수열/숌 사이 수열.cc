#include <bits/stdc++.h>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
vector<vector<int>> numlists;
int n, arr[10];
vector<int> result(20, -1);

void getNumlists(int idx=0) {
	if (idx == n) { 
		numlists.push_back(result); 
		return;
	}
	for (int i = arr[idx]+1; i < n*2; i++) {
		if (result[i] == -1 && result[i-(arr[idx]+1)] == -1) {
			result[i] = arr[idx];
			result[i-(arr[idx]+1)] = arr[idx];
			getNumlists(idx + 1);
			result[i] = -1;
			result[i-(arr[idx]+1)] = -1;
		}
	}
}
int main() {
	fastio;
	cin >> n;
	for (int i = 0; i < n; i++) cin >> arr[i];
	getNumlists();
	stable_sort(numlists.begin(), numlists.end());
	if (numlists.size() == 0) {
		cout << -1 << endl;
		return 0;
	}
	for (int j = 0; j < n * 2; j++) {
		cout << numlists[0][j] << " ";
	}
	return 0;
}