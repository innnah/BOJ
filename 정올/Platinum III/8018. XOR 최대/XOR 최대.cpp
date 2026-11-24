#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int main() {
    fastio;
    int t;
    cin >> t;
    while (t--) {
        int n;
        string s;
        cin >> n >> s;

        int m = -1;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '1') {
                m = i;
                break;
            }
        }
        if (m == -1) {
            cout << 0 << endl;
            continue;
        }

        int idx0 = -1, val = 0;
        for (int i = m+1; i < n; ++i) {
            if (s[i] == '0') {
                idx0 = i; ++val;
            }
            else {
                if (val) break;
            }
        }
        idx0 -= val - 1;
        if (val == 0) {
            for (int i = 0; i < n - m - 1; ++i) cout << 1;
            cout << (m != 0) << endl;
            continue;
        }

        int start = 0, digit = n-idx0;
        if (val <= idx0 - m) start = idx0 - val;
        else start = m;

        for (int i = m; i < idx0; ++i) cout << s[i];
        int a = idx0, b = start;
        while (digit--) {
            cout << ((s[a] - 48) ^ (s[b] - 48));
            ++a; ++b;
        }
        cout << endl;
    }
    return 0;
}