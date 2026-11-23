#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

int n, m, h;
pair<int, int> home;
int village[11][11];
vector<pair<int, int>> milks;
bool eaten[11];
int best;

void solution(int x, int y, int current, int heart) {
	if (heart < 0) return;
	if (x == home.second && y == home.first && current != 0) {
		best = max(best, current-1);
		return;
	}
	for (int i = 0; i < milks.size(); i++) {
		int nx = milks[i].second, ny = milks[i].first;
        int minus = abs(x-nx)+abs(y-ny);
		if (!eaten[i] && heart >= minus) {
			eaten[i] = true;
			solution(nx, ny, current+1, heart-minus+h);
			eaten[i] = false;
		}
	}
}
int main() {
	fastio;
	cin >> n >> m >> h;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> village[i][j];
			if (village[i][j] == 1) {
				home.first = i;
				home.second = j;
				milks.push_back(make_pair(i, j));
			}
			else if (village[i][j] == 2) {
				milks.push_back(make_pair(i, j));
			}
		}
	}
	best = 0;
	solution(home.second, home.first, 0, m);
	cout << best << endl;
}