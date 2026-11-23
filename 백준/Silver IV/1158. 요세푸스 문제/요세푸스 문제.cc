#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

int main() {
	int n, k;
	cin >> n; cin >> k;
	queue<int> q;
	int ret[5001];
	for (int i = 1; i <= n; i++) {
		q.push(i);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < k - 1; j++) {
			int tmp = q.front();
			q.pop();
			q.push(tmp);
		}
		ret[i] = q.front();
		q.pop();
	}
	string willPrint = "<";
	for (int i = 0; i < n; i++) {
		willPrint += to_string(ret[i]);
		if (i != n - 1) {
			willPrint += ", ";
		}
	}
	cout << willPrint << ">" << endl;
	return 0;
}