#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

const int MAX = 300127;
ll n, fmx[MAX], fmn[MAX], bmx[MAX], bmn[MAX];
pair<ll, ll> arr[MAX];
bool solve(ll d) {
    int i = 0, j = 0;
    while (i < n) {
        while (j < n && arr[j].first - arr[i].first <= d) {
            ll mx = 0, mn = 0;
            if (i > 0) {
                mx = fmx[i - 1];
                mn = fmn[i - 1];
            }
            if (j < n - 1) {
                mx = max(mx, bmx[j + 1]);
                mn = min(mn, bmn[j + 1]);
            }
            if (mx - mn <= d) return true;
            j += 1;
        }
        if (j == n) j -= 1;
        i += 1;
    }
    return false;
}
int main() {
    fastio;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i].first >> arr[i].second;
    }
    sort(arr, arr + n);
    fmx[0] = fmn[0] = arr[0].second;
    bmx[n - 1] = bmn[n - 1] = arr[n - 1].second;
    for (int i = 1; i < n; ++i) {
        fmx[i] = max(fmx[i - 1], arr[i].second);
        fmn[i] = min(fmn[i - 1], arr[i].second);
        bmx[n - i - 1] = max(bmx[n - i], arr[n - i - 1].second);
        bmn[n - i - 1] = min(bmn[n - i], arr[n - i - 1].second);
    }

    ll lo = 0, hi = 2000000000;
    while (lo + 1 < hi) {
        int mid = (lo + hi) / 2;
        if (solve(mid)) {
            hi = mid;
        }
        else {
            lo = mid + 1;
        }
    }
    ll ans = hi;
    if (solve(lo)) ans = lo;
    cout << ans / 2 << "." << ans % 2 * 5;
    return 0;
}