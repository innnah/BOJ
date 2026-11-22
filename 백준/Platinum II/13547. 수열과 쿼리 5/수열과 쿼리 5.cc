#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

struct Query {
    int i, j, idx;
};
int n, q, arr[1004000], q_ans[1004000], cnt[1004000], sqrt_N;
bool comp(Query A, Query B)
{
    if (A.i / sqrt_N == B.i / sqrt_N) return A.j < B.j;
    return A.i < B.i;
}
int main() {
    fastio;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    cin >> q;
    sqrt_N = sqrt(n);
    vector<Query> querys;
    for (int i = 0; i < q; ++i) {
        Query tmp;
        cin >> tmp.i >> tmp.j;
        --tmp.i;
        tmp.idx = i;
        querys.push_back(tmp);
    }
    sort(querys.begin(), querys.end(), comp);
    int l = querys[0].i, r = querys[0].j, diff = 0;
    for (int i = l; i < r; ++i)
        if (!cnt[arr[i]]++) ++diff;
    q_ans[querys[0].idx] = diff;
    for (int i = 1; i < q; ++i) {
        while (querys[i].i < l) if (!cnt[arr[--l]]++) ++diff;
        while (querys[i].j > r) if (!cnt[arr[r++]]++) ++diff;
        while (querys[i].i > l) if (!--cnt[arr[l++]]) --diff;
        while (querys[i].j < r) if (!--cnt[arr[--r]]) --diff;
        q_ans[querys[i].idx] = diff;
    }
    for (int i = 0; i < q; ++i) {
        cout << q_ans[i] << endl;
    }
    return 0;
}