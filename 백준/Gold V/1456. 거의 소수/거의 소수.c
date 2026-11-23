#include <stdio.h>
#include <math.h>
#include <stdbool.h>

typedef long long ll;

bool isNotPrime[10000001];

void sieve(const int n) {
    isNotPrime[0] = true;
    isNotPrime[1] = true;

    int m = sqrt((double)n);
    for (int i = 2; i <= m; i++) {
        if (!isNotPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isNotPrime[j] = true;
            }
        }
    }
}

int main() {
	ll a, b;
	scanf("%lld %lld", &a, &b);
    sieve((int)sqrt((double)b) + 1);
    int cnt = 0;
    for (int i = 2; i <= (int)sqrt((double)b); i++) {
        int multi = 2;
        if (!isNotPrime[i]) {
            while (pow(i, multi) <= b) {
                if (pow(i, multi) >= a) {
                    cnt += 1;
                }
                multi += 1;
            }
        }
    }
    printf("%d\n", cnt);
	return 0;
}