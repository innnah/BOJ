#include <bits/stdc++.h>

using namespace std;

int n, k, arr[5000001];
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    cin >> n >> k;
    for (int i = 0; i < n; ++i) cin >> arr[i];
    for (int i = 0; i < n; ++i) {
        pq.push({arr[i], i});
        while (pq.top().second < i-k+1) pq.pop();
        cout << pq.top().first << " ";
    }
}