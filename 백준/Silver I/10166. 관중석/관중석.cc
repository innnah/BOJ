#include <bits/stdc++.h>

using namespace std;

bool a[2001][2001];
int gcd(int a, int b) {
    while (b != 0) {
        int tmp = a;
        a = b, b = tmp % b;
    }
    return a;
}
int main() {
    int n, m, ret = 0;
    cin >> n >> m;
    for (int i = n; i <= m; ++i) {
        for (int j = 0; j < i; ++j) {
            int g = gcd(i, j);
            int x = j/g, y = i/g;
            if (!a[x][y]) {
                ret += 1;
                a[x][y] = 1;
            }
        }
    }
    cout << ret;
    return 0;
}