#include <bits/stdc++.h>
using namespace std;

class SegTree {
public:
    int n;
    vector<int> arr;
    vector<int> tree;

    SegTree(vector<int>& l) {
        n = l.size();
        arr = l;
        tree = vector<int>(n * 4 + 1, 0);
        makeTree(1, 0, n - 1);
    }

    int makeTree(int v, int s, int e) {
        if (s == e) {
            tree[v] = arr[s];
            return tree[v];
        }
        int mid = (s + e) / 2;
        tree[v] = min(makeTree(v * 2, s, mid), makeTree(v * 2 + 1, mid + 1, e));
        return tree[v];
    }

    int query(int l, int r) {
        return __query(1, 0, n - 1, l, r);
    }

    int __query(int v, int s, int e, int l, int r) {
        if (l > e || r < s) return 987654321;
        if (l <= s && e <= r) return tree[v];
        int mid = (s + e) / 2;
        return min(__query(v * 2, s, mid, l, r), __query(v * 2 + 1, mid + 1, e, l, r));
    }

    void update(int idx, int val) {
        __update(1, 0, n - 1, idx, val);
    }

    int __update(int v, int s, int e, int idx, int val) {
        if (idx < s || idx > e) return tree[v];
        if (s == e) {
            tree[v] = val;
            return tree[v];
        }
        int mid = (s + e) / 2;
        tree[v] = min(__update(v * 2, s, mid, idx, val), __update(v * 2 + 1, mid + 1, e, idx, val));
        return tree[v];
    }
};

int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<int> arr(n);
        vector<int> marr(n);

        for (int i = 0; i < n; i++) {
            arr[i] = i;
            marr[i] = -i;
        }

        SegTree segmin(arr);
        SegTree segmax(marr);

        for (int i = 0; i < m; i++) {
            int q, a, b;
            cin >> q >> a >> b;
            if (q) {
                int minval = segmin.query(a, b);
                int maxval = -segmax.query(a, b);
                if (minval == a && maxval == b) {
                    cout << "YES\n";
                }
                else {
                    cout << "NO\n";
                }
            }
            else {
                int v1 = segmin.query(a, a);
                int v2 = segmin.query(b, b);
                segmin.update(a, v2);
                segmin.update(b, v1);

                v1 = segmax.query(a, a);
                v2 = segmax.query(b, b);
                segmax.update(a, v2);
                segmax.update(b, v1);
            }
        }
    }
    return 0;
}