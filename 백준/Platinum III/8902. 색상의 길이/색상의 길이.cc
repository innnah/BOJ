#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

string s[2];
int arr[2][5027], dp[5027][5027];
pair<int, int> pla[2][26];
int dpf(int idx1, int idx2) {
    if (idx1 == s[0].length() && idx2 == s[1].length()) return 0;
    if (dp[idx1][idx2] != 300000) return dp[idx1][idx2];
    if (idx1 != s[0].length()) {
        int tmp = 0;
        if ((arr[0][idx1] == 1 || arr[0][idx1] == 3) && pla[1][s[0][idx1] - 65].first >= idx2) tmp -= idx1 + idx2;
        if ((arr[0][idx1] == 2 || arr[0][idx1] == 3) && pla[1][s[0][idx1] - 65].second < idx2) tmp += idx1 + idx2;
        //cout << idx1 << " " << idx2 << " " << tmp << endl;
        dp[idx1][idx2] = min(dp[idx1][idx2], dpf(idx1 + 1, idx2) + tmp);
    }
    if (idx2 != s[1].length()) {
        int tmp = 0;
        if ((arr[1][idx2] == 1 || arr[1][idx2] == 3) && pla[0][s[1][idx2] - 65].first >= idx1) tmp -= idx1 + idx2;
        if ((arr[1][idx2] == 2 || arr[1][idx2] == 3) && pla[0][s[1][idx2] - 65].second < idx1) tmp += idx1 + idx2;
        //cout << idx1 << " " << idx2 << " " << tmp << endl;
        dp[idx1][idx2] = min(dp[idx1][idx2], dpf(idx1, idx2 + 1) + tmp);
    }
    return dp[idx1][idx2];
}
int main() {
    fastio;
    int t;
    cin >> t;
    while (t--) {
        cin >> s[0] >> s[1];
        for (int k = 0; k < 2; ++k) {
            for (int i = 0; i < 26; ++i) {
                pla[k][i].first = 300000;
                pla[k][i].second = -300000;
            }
            for (int i = 0; i < s[k].length(); ++i) {
                arr[k][i] = 0;
            }
        }
        set<char> t[2];
        for (int k = 0; k < 2; ++k) {
            for (int i = 0; i < s[k].length(); ++i) {
                if (find(t[k].begin(), t[k].end(), s[k][i]) == t[k].end()) {
                    t[k].insert(s[k][i]);
                    arr[k][i] += 1;
                    pla[k][s[k][i] - 65].first = i;
                }
            }
        }

        t[0].clear(); t[1].clear();
        for (int k = 0; k < 2; ++k) {
            for (int i = s[k].length()-1; i >= 0; --i) {
                if (find(t[k].begin(), t[k].end(), s[k][i]) == t[k].end()) {
                    t[k].insert(s[k][i]);
                    arr[k][i] += 2;
                    pla[k][s[k][i] - 65].second = i;
                }
            }
        }

        for (int i = 0; i <= s[0].length(); ++i) {
            for (int j = 0; j <= s[1].length(); ++j) {
                dp[i][j] = 300000;
            }
        }
        cout << dpf(0, 0) << endl;
    }
    return 0;
}