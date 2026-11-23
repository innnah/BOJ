#include <bits/stdc++.h>

using ll = long long;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

ll xorval, sum, x;
int no, m;
int main() {
	fastio;
	cin >> m;
	while (m--) {
		cin >> no;
		if (no == 1 || no == 2) cin >> x;
		if (no == 1) {
			sum += x;
			xorval ^= x;
		}
		else if (no == 2) {
			sum -= x;
			xorval ^= x;
		}
		else if (no == 3) {
			cout << sum << endl;
		}
		else if (no == 4) {
			cout << xorval << endl;
		}
	}
    return 0;
}