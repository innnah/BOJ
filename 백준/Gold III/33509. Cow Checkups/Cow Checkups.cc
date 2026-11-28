#include <bits/stdc++.h>
using namespace std;

int n, a[7512], b[7512], cnt[7512];
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        cin >> b[i];
    }
    
    int score = 0;
    for (int i = 0; i < n; ++i) {
        score += (a[i] == b[i]);
    }
    
    for (int i = 0; i < n; ++i) {
        int s = 0;
        for (int j = 0; j <= min(i, n-1-i); ++j) {
            int s1 = (a[i-j] == b[i-j]), s2 = (a[i+j] == b[i+j]);
            s += (a[i-j] == b[i+j])-s1;
            s += (a[i+j] == b[i-j])-s2;
            cnt[score+s]++;
            //cout << score+s << endl;
        }
    }
    
    for (int i = 0; i < n-1; ++i) {
        int s = 0;
        for (int j = 0; j <= min(i, n-1-i-1); ++j) {
            int s1 = (a[i-j] == b[i-j]), s2 = (a[i+1+j] == b[i+1+j]);
            s += (a[i-j] == b[i+1+j])-s1;
            s += (a[i+1+j] == b[i-j])-s2;
            cnt[score+s]++;
            //cout << score+s << endl;
        }
    }
    
    for (int i = 0; i <= n; ++i) {
        cout << cnt[i] << "\n";
    }
    return 0;
}