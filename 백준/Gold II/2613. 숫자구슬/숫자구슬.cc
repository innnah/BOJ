#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, m;
int arr[305], cache[305][305];
pair<int, int> trace[305][305];
const int INF = 987654321;
int solve(int idx, int parts) {
    if (idx == n && parts == 0) return 0;
    if (parts == 0) return INF;
    int& ret = cache[idx][parts];
    if (ret != -1) return ret;
    int sum = 0;
    ret = INF;
    for (int i = idx; i < n; ++i) {
        sum += arr[i];
        int cand = max(sum, solve(i + 1, parts - 1));
        if (ret > cand) {
            ret = cand;
            trace[idx][parts] = { i + 1, parts - 1 };
        }
    }
    return ret;
}
void reconstruct(int idx, int parts) {
    if (idx >= n) return;
    cout << trace[idx][parts].first - idx << " ";
    reconstruct(trace[idx][parts].first, trace[idx][parts].second);
}
int main() {
    fastio;
    memset(cache, -1, sizeof(cache));
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    cout << solve(0, m) << endl;
    reconstruct(0, m);
    return 0;
}