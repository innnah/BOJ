#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
#define pii pair<int, int>
typedef tree<pii,null_type,less<pii>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;

ordered_set s;
int n, k;
int arr[250005];
int main() {
    fastio
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    long long ret = 0;
    for (int i = 0; i < k; ++i) {
        s.insert({arr[i], i});
    }
    ret += (*s.find_by_order((k+1)/2-1)).first;
    for (int i = k; i < n; ++i) {
        s.erase({arr[i-k], i-k});
        s.insert({arr[i], i});
        ret += (*s.find_by_order((k+1)/2-1)).first;
    }
    cout << ret;
    return 0;
}