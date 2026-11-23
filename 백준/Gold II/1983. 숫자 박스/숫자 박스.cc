#include <bits/stdc++.h>

using namespace std;

const int INF = 987654321;
int n, blank1, blank2, box1[404], box2[404], cache[404][404][404];
vector<int> num1, num2;
int dp(int place, int idxA, int idxB) {
    if (place == n) { 
        return ((idxA == num1.size() && idxB == num2.size()) - 1) * INF;
    }
    int& ret = cache[place][idxA][idxB];
    if (ret != -INF) return ret;
    bool blaA = place-idxA < blank1;
    bool blaB = place-idxB < blank2;
    bool fillA = idxA < num1.size();
    bool fillB = idxB < num2.size();
    if (blaA && blaB) {
        int cand = dp(place+1, idxA, idxB);
        ret = max(ret, cand);
    }
    if (blaA && fillB) {
        int cand = dp(place+1, idxA, idxB+1);
        ret = max(ret, cand);
    }
    if (fillA && blaB) {
        int cand = dp(place+1, idxA+1, idxB);
        ret = max(ret, cand);
    }
    if (fillA && fillB) {
        int cand = dp(place+1, idxA+1, idxB+1) + num1[idxA] * num2[idxB];
        ret = max(ret, cand);
    }
    return ret;
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            for (int k = 0; k < n; ++k)
                cache[i][j][k] = -INF;
    for (int i = 0; i < n; ++i) {
        cin >> box1[i];
        if (box1[i]) num1.push_back(box1[i]);
    }
    for (int i = 0; i < n; ++i) {
        cin >> box2[i];
        if (box2[i]) num2.push_back(box2[i]);
    }
    blank1 = n - num1.size();
    blank2 = n - num2.size();
    cout << dp(0, 0, 0) << endl;
    return 0;
}