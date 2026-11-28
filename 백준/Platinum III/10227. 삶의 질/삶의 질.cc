#include <bits/stdc++.h>

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

#define fastio ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define endl "\n"

int r, c, h, w, arr[3127][3127], psum[3127][3127], tmp[3127][3127];
inline int get_sum(int r1, int c1, int r2, int c2) {
    return psum[r2][c2] - psum[r2][c1] - psum[r1][c2] + psum[r1][c1];
}
int main() {
    fastio;
    cin >> r >> c >> h >> w;
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            cin >> arr[i][j];

    int lo = 1, hi = r * c, md = (h*w-1)/2;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j) {
                if (arr[i][j] > mid) tmp[i][j] = 1;
                else tmp[i][j] = 0;
            }
        for (int i = 0; i < r; ++i)
            for (int j = 0; j < c; ++j)
                psum[i+1][j+1] = psum[i+1][j] + psum[i][j+1] - psum[i][j] + tmp[i][j];
        
        bool flag = false;
        for (int i = h - 1; i < r; ++i) {
            for (int j = w-1; j < c; ++j)
                if (get_sum(i - h + 1, j - w + 1, i + 1, j + 1) <= md) {
                    hi = mid;
                    flag = true;
                    break;
                }
            if (flag) break;
        }
        if (!flag) lo = mid + 1;
    }
    cout << lo;
    return 0;
}