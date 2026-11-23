#include <bits/stdc++.h>

using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

string h, n;
vector<int> getPi(string& s) {
    int n = s.size();
    int j = 0;
    vector<int> pi(n + 1, 0);
    for (int i = 1; i < n; i++) {
        while (j > 0 && s[i] != s[j]) j = pi[j];
        if (s[i] == s[j]) pi[i + 1] = ++j;
    }
    return pi;
}
void kmp(string& h, string& n) {
    int a = h.size(), b = n.size();
    vector<int> kmpi(a), pi = getPi(n);
    string r;
    int matched = 0;
    for (int i = 0; i < a; ++i) {
        while (matched > 0 && h[i] != n[matched]) matched = pi[matched];
        r += h[i];
        if (h[i] == n[matched]) {
            ++matched;
            if (matched == b) {
                for (int i = 0; i < b; ++i) r.pop_back();
                matched = kmpi[r.size()];
            }
        }
        kmpi[r.size()] = matched;
    }
    cout << r;
}
int main() {
	fastio;
    cin >> h;
    cin >> n;
    kmp(h, n);
	return 0;
}