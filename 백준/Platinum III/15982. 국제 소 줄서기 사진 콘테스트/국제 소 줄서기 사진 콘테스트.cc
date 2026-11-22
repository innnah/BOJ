#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

int n, m, arr[100127], querys[100127], psum_arr[100127];
set<int> s[200127];
int main() {
    fastio;
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        arr[i] = arr[i] * 2 - 1;
    }
    for (int i = 0; i < m; ++i) {
        cin >> querys[i];
        --querys[i];
    }
    s[n].insert(-1);
    int psum = 0;
    for (int i = 0; i < n; ++i) {
        psum += arr[i];
        psum_arr[i] = psum;
        s[psum + n].insert(i);
    }
    multiset<int> cands;
    for (int i = 0; i <= 2 * n; ++i) {
        if (!s[i].empty()) {
            cands.insert(*s[i].rbegin() - *s[i].begin());
        }
    }
    cout << *cands.rbegin() << endl;
    for (int i = 0; i < m; ++i) {
        int q = querys[i];
        if (arr[q] != arr[q + 1]) {
            //cands.erase(*s[psum_arr[q] + n].rbegin() - *s[psum_arr[q] + n].begin());
            cands.erase(cands.find(*s[psum_arr[q] + n].rbegin() - *s[psum_arr[q] + n].begin()));
            s[psum_arr[q] + n].erase(q);

            int tmp = psum_arr[q];
            psum_arr[q] += arr[q + 1] - arr[q];

            //cands.erase(*s[psum_arr[q] + n].rbegin() - *s[psum_arr[q] + n].begin());
            if (!s[psum_arr[q] + n].empty())
                cands.erase(cands.find(*s[psum_arr[q] + n].rbegin() - *s[psum_arr[q] + n].begin()));
            s[psum_arr[q] + n].insert(q);
            swap(arr[q], arr[q + 1]);

            if (!s[tmp + n].empty()) cands.insert(*s[tmp + n].rbegin() - *s[tmp + n].begin());
            if (!s[psum_arr[q] + n].empty()) cands.insert(*s[psum_arr[q] + n].rbegin() - *s[psum_arr[q] + n].begin());
        }
        cout << *cands.rbegin() << endl;
    }
    return 0;
}