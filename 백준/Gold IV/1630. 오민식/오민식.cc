#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

const ll MOD = 987654321;
const int MAX = pow(10, 6);
int n;
ll ret = 1L;
unsigned char isPrime[(MAX+7)/8];
inline bool is_prime(int k) {
    return isPrime[k>>3] & (1<<(k&7));
}
inline void setComposite(int k) {
    isPrime[k>>3] &= ~(1<<(k&7));
}
void sieve(int n) {
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
int intlog(double base, double x) {
    return (int)(log(x) / log(base));
}
int main() {
	fastio;
    memset(isPrime, 255, sizeof(isPrime));
    sieve(MAX);
    cin >> n;
    for (int i = 2; i <= n; i++) {
        if (is_prime(i)) ret = (ret * (ll)pow(i, intlog(i, n))) % MOD;
    }
    cout << ret << endl;
	return 0;
}