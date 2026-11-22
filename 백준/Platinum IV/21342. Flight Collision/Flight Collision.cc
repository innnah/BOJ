#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

struct Query {
    ll a, b, idx1, idx2;
};

ll gcd(ll a, ll b) {
    while (a != 0) {
        ll tmp = a;
        a = b % a, b = tmp;
    }
    return b;
}

int n;
pair<ll, ll> arr[100127];
int main() {
    fastio;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i].first >> arr[i].second;
    }

    auto comp = [](const Query x, const Query y) {
        if (x.a * y.b == x.b * y.a) return make_pair(x.idx1, x.idx2) < make_pair(y.idx1, y.idx2);
        return x.a * y.b < x.b * y.a;
        };
    set<Query, decltype(comp)> v(comp);
    set<ll> s;
    s.insert(0);
    for (int i = 1; i < n; ++i) {
        s.insert(i);
        ll tmp1 = arr[i - 1].second - arr[i].second, tmp2 = arr[i].first - arr[i - 1].first;
        if (tmp1 <= 0) continue;
        ll g = gcd(tmp1, tmp2);
        tmp1 /= g; tmp2 /= g;
        v.insert({ tmp2, tmp1, i - 1, i });
    }
    while (!v.empty()) {
        Query a = *v.begin();
        v.erase(v.begin());
        if (s.find(a.idx1) == s.end() || s.find(a.idx2) == s.end()) continue;
        s.erase(a.idx1); s.erase(a.idx2);
        set<ll>::iterator iter = s.lower_bound(a.idx1);
        if (iter != s.begin() && iter != s.end()) {
            ll idx2 = *iter, idx1 = *(--iter);
            ll tmp1 = arr[idx1].second - arr[idx2].second, tmp2 = arr[idx2].first - arr[idx1].first;
            if (tmp1 <= 0) continue;
            ll g = gcd(tmp1, tmp2);
            tmp1 /= g; tmp2 /= g;
            v.insert({ tmp2, tmp1, idx1, idx2 });
        }
    }
    cout << s.size() << endl;
    for (auto& i : s) {
        cout << i+1 << " ";
    }
    return 0;
}