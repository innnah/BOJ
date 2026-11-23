#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	string s, t;
	bool broken = false;
	cin >> s >> t;
	while (t.length() >= s.length()) {
		if (t == s) {
			cout << 1 << endl;
			broken = true;
			break;
		}
		char last = *(t.end()-1);
		t.pop_back();
		if (t.length() == 0) {
			break;
		}
		if (last == 'B') {
			reverse(t.begin(), t.end());
		}
	}
	if (!broken) {
		cout << 0 << endl;
	}
	return 0;
}