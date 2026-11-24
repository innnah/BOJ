#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int n, k;
queue<pair<int, int>> row[100005];
pair<int, int> customer[100005];
vector<int> finished;
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        cin >> customer[i].first >> customer[i].second;
    }
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    for (int i = 0; i < k; ++i) {
        pq.push({0, i});
    }
    for (int i = 0; i < n; ++i) {
        pair<int, int> tmp = pq.top();
        pq.pop();
        row[tmp.second].push(customer[i]);
        pq.push({tmp.first+customer[i].second, tmp.second});
    }
    while (finished.size() < n) {
        for (int i = k-1; i >= 0; --i) {
            if (!row[i].empty()) {
                row[i].front().second -= 1;
                if (row[i].front().second == 0) {
                    finished.push_back(row[i].front().first);
                    row[i].pop();
                }
            }
        }
    }
    long long ret = 0;
    for (int i = 0; i < n; ++i) {
        ret += (long long)finished[i] * (i+1);
    }
    cout << ret;
    return 0;
}