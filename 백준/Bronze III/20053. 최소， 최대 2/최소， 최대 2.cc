#include <bits/stdc++.h>

using namespace std;
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
int t, n, num;
int main() {
    fastio;
    cin >> t;
    while (t--) {
        cin >> n;
        int mini=1000001, maxi=-1000001;
        while (n--) {
            cin >> num;
            if (num < mini) mini = num;
            if (num > maxi) maxi = num;
        }
        cout << mini << " " << maxi << "\n";
    }
    return 0;
}