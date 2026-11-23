#pragma GCC optimize('Ofast')
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"

int t;
string a, w, s;

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
bool kmp(const string& a, const string& b) {
    int n = a.size(), m = b.size();
    vector<int> pi = getPi(b);
    int begin = 0, matched = 0;
    bool flag = false;
    while (begin <= n - m) {
        if (matched < m && a[begin + matched] == b[matched]) {
            ++matched;
            if (matched == m) {
                if (!flag) flag = true;
                else return false;
            }
        }
        else {
            if (matched == 0) begin += 1;
            else {
                begin += matched - pi[matched];
                matched = pi[matched];
            }
        }
    }
    return flag;
}

int main() {
	fastio;
	cin >> t;
	while (t--) {
		cin >> a >> w >> s;
		map<char, char> conv;
        vector<int> result;
        for (int i = 0; i < a.length(); ++i) {
            conv.insert(make_pair(a[i], a[(i + 1) % a.length()]));
        }
		for (int i = 0; i < a.length(); ++i) {
			bool ret = kmp(s, w);
            if (ret) result.push_back(i);
            for (int i = 0; i < w.length(); ++i) {
                w[i] = conv[w[i]];
            }
		}
        if (result.size() == 0) cout << "no solution";
        else if (result.size() == 1) cout << "unique: " << result[0];
        else {
            cout << "ambiguous: ";
            for (auto i = result.begin(); i != result.end(); ++i) {
                cout << *i << " ";
            }
        }
        cout << endl;
	}
	return 0;
}