#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define __builtin_popcount __popcnt

const int MAX = 200127;
ll n;
pair<int, ll> tree[MAX * 4];
vector<ll> arr;
vector<pair<ll, ll>> arr2;
map<ll, int> m;
vector<pair<ll, int>> q1;
vector<pair<ll, int>> q2;
vector<ll> q3;
int query(ll k, int v, int s, int e) {
    if (s == e) {
        //cout << s << " " << e << " " << tree[v].second << " " << k << endl;
        if (tree[v].second == k) return -1;
        return (tree[v].second <= k) * tree[v].first;
    }
    int mid = (s + e) / 2;
    //cout << s << " " << e << " " << tree[v].second << " " << k << endl;
    if (tree[v * 2].second < k) {
        int sub = query(k, v * 2 + 1, mid + 1, e);
        if (sub == -1) return sub;
        return tree[v * 2].first + sub;
    }
    return query(k, v * 2, s, mid);
}
pair<int, ll> update(int idx, ll val, int v, int s, int e) {
    if (idx < s || idx > e) return tree[v];
    if (s == e) {
        tree[v] = { tree[v].first + 1, val };
        return tree[v];
    }
    int mid = (s + e) / 2;
    pair<int, ll> le = update(idx, val, v * 2, s, mid), ri = update(idx, val, v * 2 + 1, mid + 1, e);
    return tree[v] = { le.first + ri.first, max(le.second, ri.second) };
}
int main() {
    fastio;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int qn;
        cin >> qn;
        if (qn == 1) {
            pair<ll, ll> p;
            cin >> p.first >> p.second;
            if (p.first) {
                ll a = p.first, b = p.second;
                if (a < 0) {
                    b = -b;
                    a = -a;
                }
                ll tmp;
                tmp = (-b / a) * 2;
                ll t2 = -b % a;
                if (t2 < 0) --tmp;
                else if (t2 > 0) ++tmp;
                arr.push_back(tmp);
                arr2.push_back(p);
                q1.push_back({ tmp, i });
            }
            else {
                q3.push_back(p.second);
            }
        }
        else {
            ll a;
            cin >> a;
            q2.push_back({ a * 2, i });
        }
    }
    sort(arr.begin(), arr.end());
    for (int i = 0; i < arr.size(); ++i) {
        m[arr[i]] = i;
    }
    for (int i = 1; i <= n * 4 + 8; ++i) {
        tree[i].second = -2000000000000000001LL;
    }
    int idx1 = 0, idx2 = 0, idx3 = 0, st = 1;
    for (int i = 0; i < n; ++i) {
        if (idx1 < q1.size() && q1[idx1].second == i) {
            pair<ll, int> tmp = q1[idx1];
            pair<ll, ll> tmp2 = arr2[idx1];
            //cout << tmp2.first << " " << tmp2.second << endl;
            update(m[tmp.first], tmp.first, 1, 0, n - 1);
            if (tmp2.first > 0) st *= -1;
            ++idx1;
        }
        else if (idx2 < q2.size() && q2[idx2].second == i) {
            ll a = q2[idx2].first;
            int qr = query(a, 1, 0, n - 1);
            if (qr == -1) cout << 0 << endl;
            else {
                int val = st * pow(-1, qr % 2);
                if (val == -1) cout << "-" << endl;
                else if (val == 1) cout << "+" << endl;
                else cout << 0 << endl;
            }
            ++idx2;
        }
        else {
            if (q3[idx3] < 0) st *= -1;
            else if (q3[idx3] == 0) st = 0;
            ++idx3;
        }
    }
    return 0;
}