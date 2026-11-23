#include <cstdio>
#include <vector>

typedef long long ll;
using namespace std;

vector<int> solution(int n, int m) {
	vector<int> v(m);
	ll sum = 0L;
	for (int i = 0; i < m; i++) {
		v[i] = i;
		sum += i;
	}
	if (n < sum) {
		return vector<int>(1, -1);
	}
	n -= sum;
	if (n % m == 0) {
		for (auto& i : v) {
			i += n / m;
		}
		return v;
	}
	return vector<int>(1, -1);
}

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	int end = (n > 100 ? 100 : n);
	for (int i = m; i <= 100; i++) {
		vector<int> v = solution(n, i);
		if (v.size() > 1) {
			for (auto& j : v) {
				printf("%d ", j);
			}
			return 0;
		}
	}
	printf("%d", -1);
	return 0;
}