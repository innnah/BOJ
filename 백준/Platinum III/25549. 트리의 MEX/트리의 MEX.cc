#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int n, tree[800127], arr[200127], mex[200127];
set<int> mexset[200127];
vector<int> graph[200127];
void dfs(int v) {
    if (graph[v].empty()) {
        mex[v] = (arr[v] == 0);
        return;
    }
    int mx = graph[v][0], maxans = 0;
    for (auto& i : graph[v]) {
        dfs(i);
        if (mexset[i].size() > mexset[mx].size()) mx = i;
        maxans = max(maxans, mex[i]);
    }
    mexset[mx].insert(arr[v]);
    for (auto& i : graph[v]) {
        if (i != mx) {
            for (auto& j : mexset[i]) {
                mexset[mx].insert(j);
            }
        }
    }
    swap(mexset[mx], mexset[v]);
    for (int i = maxans; i <= n; ++i) {
        if (mexset[v].find(i) == mexset[v].end()) {
            mex[v] = i;
            break;
        }
    }
}
int main() {
    fastio;
    cin >> n;
    int root = -1;
    for (int i = 0; i < n; ++i) {
        int tmp;
        cin >> tmp;
        if (tmp == -1) root = i+1;
        else graph[tmp].push_back(i + 1);
    }
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
        mexset[i].insert(arr[i]);
    }
    dfs(root);
    for (int i = 1; i <= n; ++i) {
        cout << mex[i] << endl;
    }
    return 0;
}