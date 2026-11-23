#include <string>
#include <iostream>

using namespace std;

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int n;
	cin >> n;
	while (n--) {
		string tmp, d;
		int b;
		cin >> tmp >> d;
		b = stoi(tmp);
		int mod = 0;
		for (auto& i : d) {
			string s;
			s = i;
			mod += stoi(s, NULL, b) % (b - 1);
		}
		cout << mod % (b - 1) << endl;
	}
	return 0;
}