#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <cmath>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAX = 4000000;
unsigned char isPrime[(MAX + 7) / 8];
vector<int> primes;
int n, ret;

static inline bool is_prime(int k) {
    return isPrime[k >> 3] & (1 << (k & 7));
}
static inline void setComposite(int k) {
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
int main() {
    memset(isPrime, 255, sizeof(isPrime));
    sieve2(MAX);
    scanf("%d", &n);
    for (int i = 2; i <= MAX; i++) {
        if (is_prime(i)) {
            primes.push_back(i);
        }
    }
    auto s = primes.begin(), e = primes.begin();
    int psum = 2;
    while (*e <= n) {
        if (psum == n) {
            ++ret;
        }
        if (psum > n) { 
            psum -= *s++;
        }
        else if (psum <= n) {
            ++e;
            if (e == primes.end()) break;
            psum += *e;
        }
    }
    printf("%d", ret);
	return 0;
}