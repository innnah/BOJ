#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

const int MAX = 100000000;
unsigned char isPrime[(MAX + 7) / 8];
inline bool is_prime(int k) {
    return isPrime[k >> 3] & (1 << (k & 7));
}
inline void setComposite(int k) {
    isPrime[k >> 3] &= ~(1 << (k & 7));
}
void sieve2(int n) {
    setComposite(0);
    setComposite(1);
    int m = int(sqrt(n));
    for (int i = 2; i <= m; i++) {
        if (is_prime(i)) {
            for (int j = i * i; j <= n; j += i) {
                setComposite(j);
            }
        }
    }
}
int n, a, b;
int main() {
	fastio;
    memset(isPrime, 255, sizeof(isPrime));
    sieve2(MAX);
	while (1) {
		cin >> n;
		if (cin.eof()) break;
        a = b = 2;
        n -= 4;
        if (n % 2) {
            b = 3;
            n -= 1;
        }
        if (n < 4) { 
            cout << "Impossible." << endl; 
            continue;
        }
        for (int i = 2; i <= MAX / 2; i++) {
            if (is_prime(i) && is_prime(n - i)) {
                cout << a << " " << b << " " << i << " " << n - i << endl;
                break;
            }
        }
	}
	return 0;
}