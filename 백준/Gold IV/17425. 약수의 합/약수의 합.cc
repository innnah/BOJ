#include <cstdio>
#include <algorithm>

typedef long long ll;
using namespace std;

ll cache[1000001];
ll psum[1000001];

int main() {
	fill_n(cache, 1000001, 1L);
	for (int i = 2; i <= 1000000; i++) {
		for (int j = 1; j <= 1000000/i; j++) {
			cache[i * j] += i;
		}
	}
	psum[0] = 0L;
	for (int i = 1; i <= 1000000; i++) {
		psum[i] = psum[i - 1] + cache[i];
	}
	int t;
	scanf("%d", &t);
	while (t--) {
		int n;
		scanf("%d", &n);
		printf("%lld\n", psum[n]);
	}
    return 0;
}