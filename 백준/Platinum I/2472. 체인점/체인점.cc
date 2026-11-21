#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"
#define pii pair<int, int>

int n, m, ans[100127];
vector<pair<int, ll>> graph[100127];
vector<ll> dist[100127];
vector<int> apart = vector<int>(3);
ll tree[263127];
void dijkstra(int idx) {
    priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> q;
    dist[apart[idx]][idx] = 0;
    q.push({ 0, apart[idx]});
    while (!q.empty()) {
        pair<ll, int> poped = q.top();
        q.pop();
        ll cur_dist = poped.first, node = poped.second;
        if (cur_dist > dist[node][idx]) continue;
        for (int i = 0; i < graph[node].size(); ++i) {
            pair<int, int> ne = graph[node][i];
            ll cost = dist[node][idx] + ne.second;
            if (cost < dist[ne.first][idx]) {
                dist[ne.first][idx] = cost;
                q.push({ cost, ne.first });
            }
        }
    }
}
ll init(int v, int s, int e) {
    if (s == e) return tree[v] = 98765432123456789LL;
    int mid = (s + e) / 2;
    return tree[v] = min(init(v * 2, s, mid), init(v * 2 + 1, mid + 1, e));
}
ll update(int v, int s, int e, int idx, ll val) {
    if (idx < s || idx > e) return tree[v];
    if (s == e) {
        tree[v] = min(tree[v], val);
        return tree[v];
    }
    int mid = (s + e) / 2;
    return tree[v] = min(update(v * 2, s, mid, idx, val), update(v * 2 + 1, mid + 1, e, idx, val));
}
ll query(int v, int s, int e, int l, int r) {
    if (e < l || r < s) return 98765432123456789LL;
    if (l <= s && e <= r) return tree[v];
    int mid = (s + e) / 2;
    return min(query(v * 2, s, mid, l, r), query(v * 2 + 1, mid + 1, e, l, r));
}
int main() {
	fastio;
	cin >> n >> apart[0] >> apart[1] >> apart[2] >> m;
    apart[0]--; apart[1]--; apart[2]--;
	for (int i = 0; i < m; ++i) {
		int a, b;
		ll c;
        cin >> a >> b >> c; --a; --b;
		graph[a].push_back({ b, c });
		graph[b].push_back({ a, c });
	}
    for (int i = 0; i < n; ++i) {
        dist[i] = vector<ll>(6);
        dist[i][0] = dist[i][1] = dist[i][2] = 98765432123456789LL;
        dist[i][3] = i;
    }
    for (int i = 0; i < 3; ++i) dijkstra(i);
    /*
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 3; ++j) {
            cout << dist[i][j] << " ";
        }
        cout << endl;
    }
    */
    sort(dist, dist + n);
    dist[0][4] = 0;
    for (int i = 1; i < n; ++i) {
        if (dist[i - 1][0] == dist[i][0]) dist[i][4] = dist[i - 1][4];
        else dist[i][4] = dist[i - 1][4] + 1;
    }
    sort(dist, dist + n, [&](vector<ll> a, vector<ll> b) { return a[1] < b[1]; });
    for (int i = 0; i < n; ++i) dist[i][5] = i;

    init(1, 0, n-1);
    int start = 0;
    for (int i = 0; i < n; ++i) {
        if (i > 0 && dist[i - 1][1] != dist[i][1]) {
            while (start <= i) {
                update(1, 0, n - 1, dist[start][4], dist[start][2]);
                ++start;
            }
        }
        ans[dist[i][3]] = (dist[i][2] > query(1, 0, n - 1, 0, dist[i][4] - 1));
        //cout << i << " " << dist[i][2] << " " << query(1, 0, n - 1, 0, dist[i][4] - 1) << endl;
    }
    /*
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < 6; ++j) {
            cout << dist[i][j] << " ";
        }
        cout << endl;
    }
    */
    int t; cin >> t;
    while (t--) {
        int q; cin >> q;
        if (ans[q-1]) cout << "NO" << endl;
        else cout << "YES" << endl;
    }
	return 0;
}