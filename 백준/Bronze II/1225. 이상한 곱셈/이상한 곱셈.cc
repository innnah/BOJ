#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    string a, b;
    long long sa = 0, sb = 0;
    cin >> a >> b;
    for (int i = 0; i < a.size(); ++i) {
        sa += a[i] - 48;
    }
    for (int i = 0; i < b.size(); ++i) {
        sb += b[i] - 48;
    }
    cout << sa * sb;
}