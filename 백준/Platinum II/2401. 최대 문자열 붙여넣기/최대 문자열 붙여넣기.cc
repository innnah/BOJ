#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

string s;
int n;
vector<string> ss;
bitset<100005> kmp_ret[505];
int dp[100005];

vector<int> getPi(const string& s) {
    int m = s.size();
    vector<int> pi(m + 1, 0);

    int begin = 1, matched = 0;
    while (begin + matched < m) {
        if (s[begin + matched] == s[matched]) {
            ++matched;
            pi[begin + matched] = matched;
        }
        else {
            if (matched == 0) ++begin;
            else {
                begin += matched - pi[matched];
                matched = pi[matched];
            }
        }
    }
    return pi;
}

void kmp(const string a, const string b, int i) {
    int n = a.size(), m = b.size();
    vector<int> pi = getPi(b);
    int begin = 0, matched = 0;
    while (begin <= n - m) {
        if (matched < m && a[begin + matched] == b[matched]) {
            ++matched;
            if (matched == m) kmp_ret[i].set(begin);
        }
        else {
            if (matched == 0) ++begin;
            else {
                begin += matched - pi[matched];
                matched = pi[matched];
            }
        }
    }
}

int main() {
	fastio;
    cin >> s >> n;
    for (int i = 0; i < n; ++i) {
        string tmp;
        cin >> tmp;
        ss.push_back(tmp);
        kmp(s, tmp, i);
    }
    int k = s.size();
    int maximum = 0;
    for (int i = 0; i <= k; ++i) {
        maximum = max(maximum, dp[i]);
        for (int j = 0; j < n; ++j) {
            int length = ss[j].size();
            if (kmp_ret[j].test(i)) {
                dp[i + length] = max(dp[i + length], maximum + length);
            }
        }
    }
    cout << max(maximum, dp[k]) << endl;
	return 0;
}