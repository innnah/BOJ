#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    int n;
    cin >> n;
    long long a = 0, b = 1;
    while (n--) {
        long long tmp = b;
        b = a + b;
        a = tmp;
    }
    cout << (a + b) * 2;
    return 0;
}