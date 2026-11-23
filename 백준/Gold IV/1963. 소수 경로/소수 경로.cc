#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>

using namespace std;

const int MAX = 10000;
int t, s, e;
unsigned char isPrime[(MAX + 7) / 8];
bool visited[10001];

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
int bfs(int start, int end) {
    queue<pair<int,int>> q;
    q.push(make_pair(start, 0));
    visited[start] = true;
    while (!q.empty()) {
        pair<int, int> v = q.front();
        q.pop();
        if (v.first == end) return v.second;
        for (int i = 1; i < 10; i++) {
            int nv = i * 1000 + (v.first % 1000);
            if (is_prime(nv) && !visited[nv]) {
                q.push(make_pair(nv, v.second + 1));
                visited[nv] = true;
            }
        }
        for (int i = 0; i < 10; i++) {
            int nv100 = v.first / 1000 * 1000 + i * 100 + (v.first % 100);
            int nv10 = v.first / 100 * 100 + i * 10 + (v.first % 10);
            int nv1 = v.first / 10 * 10 + i;
            if (is_prime(nv100) && !visited[nv100]) {
                q.push(make_pair(nv100, v.second + 1));
                visited[nv100] = true;
            }
            if (is_prime(nv10) && !visited[nv10]) {
                q.push(make_pair(nv10, v.second + 1));
                visited[nv10] = true;
            }
            if (is_prime(nv1) && !visited[nv1]) {
                q.push(make_pair(nv1, v.second + 1));
                visited[nv1] = true;
            }
        }
    }
    return -1;
}
int main() {
	scanf("%d", &t);
    memset(isPrime, 255, sizeof(isPrime));
    sieve2(MAX);
	while (t--) {
		scanf("%d %d", &s, &e);
        memset(visited, false, sizeof(visited));
        int ret = bfs(s, e);
        if (ret == -1) printf("Impossible\n");
        else printf("%d\n", ret);
	}
	return 0;
}