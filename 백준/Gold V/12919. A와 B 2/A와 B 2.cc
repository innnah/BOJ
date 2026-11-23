#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool canMadeS(string t, string s) {
	if (t.length() < s.length()) return false;
	if (t == s) return true;
	if (*(t.end() - 1) == 'B' && t[0] != 'B') return false;
	bool ret = false;
	string tmp = t;
	if (t[0] == 'B') {
		reverse(tmp.begin(), tmp.end());
		tmp.pop_back();
		ret = ret || canMadeS(tmp, s);
	}
	if (*(t.end() - 1) != 'B') {
		tmp = t;
		tmp.pop_back();
		ret = ret || canMadeS(tmp, s);
	}
	return ret;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	string s, t;
	cin >> s >> t;
	cout << canMadeS(t, s) << endl;
	return 0;
}