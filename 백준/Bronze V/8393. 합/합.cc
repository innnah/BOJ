#include <iostream>

using namespace std;

int fastsum(int n) {
    if (n == 1) { return 1; }
    if (n % 2 == 1) { return fastsum(n-1) + n; }
    return fastsum(n/2) * 2 + (n/2) * (n/2);
}

int main() {
    int a;
    cin >> a;
    cout << fastsum(a);
}