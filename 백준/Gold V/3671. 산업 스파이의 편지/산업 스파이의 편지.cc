#include <bits/stdc++.h>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

bool isPrime[10000001];
int tc;
string num;

void sieve(int n) {
    isPrime[0] = false;
    isPrime[1] = false;

    int m = int(sqrt(n));
    for (int i = 2; i <= m; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
}
set<int> makeCombinations(string num, string made="", int taken=0) {
    set<int> ret;
    if (made != "" && isPrime[stoi(made)]) ret.insert(stoi(made));
    for (int i = 0; i < num.length(); i++) {
        if (!(taken & (1 << i))) {
            taken |= (1 << i);
            set<int> tmp = makeCombinations(num, made + num[i], taken);
            taken &= ~(1 << i);
            ret.insert(tmp.begin(), tmp.end());
        }
    }
    return ret;
}
int main() {
	fastio;
    memset(isPrime, 1, sizeof(isPrime));
    sieve(10000000);
    cin >> tc;
    while (tc--) {
        cin >> num;
        set<int> ret = makeCombinations(num);
        cout << ret.size() << endl;
    }
	return 0;
}