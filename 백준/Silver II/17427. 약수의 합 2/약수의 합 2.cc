#include <stdio.h>

typedef long long ll;
using namespace std;

int main() {
	int n;
	scanf("%d", &n);
	ll ret = 0L;
	for (int i = 1; i <= n; i++) {
		ret += n / i * i;
	}
	printf("%lld\n", ret);
	return 0;
}