#include <iostream>

#include <vector>

#include <algorithm>

using namespace std;

vector<int> arr, cnt, what, ret;

vector<vector<int>> a, tree, tree2;

vector<int> makeTree(int v, int s, int e) {

    if (s == e) {

        tree[v] = {cnt[s], s};

        return tree[v];

    }

    int mid = (s + e) / 2;

    auto v1 = makeTree(v * 2, s, mid);

    auto v2 = makeTree(v * 2 + 1, mid + 1, e);

    tree[v] = (v1[0] >= v2[0]) ? v1 : v2;

    return tree[v];

}

vector<int> query(int le, int ri, int v, int s, int e) {

    if (le > e || ri < s) return {-1, -1};

    if (le <= s && e <= ri) return tree[v];

    int mid = (s + e) / 2;

    auto v1 = query(le, ri, v * 2, s, mid);

    auto v2 = query(le, ri, v * 2 + 1, mid + 1, e);

    return (v1[0] >= v2[0]) ? v1 : v2;

}

vector<int> update(int idx, int val, int v, int s, int e) {

    if (idx < s || idx > e) return tree[v];

    if (s == e) {

        tree[v][0] += val;

        return tree[v];

    }

    int mid = (s + e) / 2;

    auto v1 = update(idx, val, v * 2, s, mid);

    auto v2 = update(idx, val, v * 2 + 1, mid + 1, e);

    tree[v] = (v1[0] >= v2[0]) ? v1 : v2;

    return tree[v];

}

vector<int> makeTree2(int v, int s, int e) {

    if (s == e) {

        tree2[v] = {what[s], s};

        return tree2[v];

    }

    int mid = (s + e) / 2;

    auto v1 = makeTree2(v * 2, s, mid);

    auto v2 = makeTree2(v * 2 + 1, mid + 1, e);

    tree2[v] = (v1[0] >= v2[0]) ? v2 : v1;

    return tree2[v];

}

vector<int> query2(int le, int ri, int v, int s, int e) {

    if (le > ri) return {1234567890, -1};

    if (le > e || ri < s) return {1234567890, -1};

    if (le <= s && e <= ri) return tree2[v];

    int mid = (s + e) / 2;

    auto v1 = query2(le, ri, v * 2, s, mid);

    auto v2 = query2(le, ri, v * 2 + 1, mid + 1, e);

    return (v1[0] >= v2[0]) ? v2 : v1;

}

vector<int> update2(int idx, int val, int v, int s, int e) {

    if (idx < s || idx > e) return tree2[v];

    if (s == e) {

        tree2[v][0] = val;

        return tree2[v];

    }

    int mid = (s + e) / 2;

    auto v1 = update2(idx, val, v * 2, s, mid);

    auto v2 = update2(idx, val, v * 2 + 1, mid + 1, e);

    tree2[v] = (v1[0] >= v2[0]) ? v2 : v1;

    return tree2[v];

}

int main() {

    int n;

    cin >> n;

    arr.resize(n);

    cnt.assign(n + 1, 0);

    a.resize(n + 1);

    for (int i = 0; i < n; ++i) {

        cin >> arr[i];

        cnt[arr[i]] += 1;

    }

    for (int i = n - 1; i >= 0; --i) {

        a[arr[i]].push_back(i);

    }

    tree.assign(4 * n + 120, vector<int>(2, 0));

    tree2.assign(4 * n + 120, vector<int>(2, 0));

    makeTree(1, 0, n);

    what.assign(n + 1, 0);

    for (int i = 0; i <= n; ++i) {

        if (!a[i].empty()) {

            what[i] = a[i].back();

        } else {

            what[i] = 1234567890;

        }

    }

    makeTree2(1, 0, n);

    for (int i = 0; i < n; ++i) {

        int confident = -1;

        auto v = tree[1];

        if (n - i - v[0] < v[0]) {

            confident = v[1];

        }

        if (confident == -1) {

            if (!ret.empty()) {

                auto v1 = query2(1, arr[ret.back() - 1] - 1, 1, 0, n);

                auto v2 = query2(arr[ret.back() - 1] + 1, n, 1, 0, n);

                auto val = (v1[0] <= v2[0]) ? v1 : v2;

                a[val[1]].pop_back();

                cnt[val[1]] -= 1;

                if (!a[val[1]].empty()) {

                    update2(val[1], a[val[1]].back(), 1, 0, n);

                } else {

                    update2(val[1], 98765432123456789, 1, 0, n);

                }

                update(val[1], -1, 1, 0, n);

                ret.push_back(val[0] + 1);

            } else {

                auto val = query2(1, n, 1, 0, n);

                a[val[1]].pop_back();

                cnt[val[1]] -= 1;

                if (!a[val[1]].empty()) {

                    update2(val[1], a[val[1]].back(), 1, 0, n);

                } else {

                    update2(val[1], 1234567890, 1, 0, n);

                }

                update(val[1], -1, 1, 0, n);

                ret.push_back(val[0] + 1);

            }

        } else {

            if (!a[confident].empty() && (ret.empty() || arr[ret.back() - 1] != confident)) {

                int v = a[confident].back();

                a[confident].pop_back();

                cnt[confident] -= 1;

                ret.push_back(v + 1);

                update(confident, -1, 1, 0, n);

            } else {

                cout << -1 << endl;

                return 0;

            }

        }

    }

    for (int i = 0; i < ret.size(); ++i) {

        cout << ret[i] << " ";

    }

    cout << endl;

    return 0;

}

