#include <bits/stdc++.h>
using namespace std;
int main(){
    unsigned int n;
    cin>>n;
    unsigned int limit = pow(2, 30);
    for(unsigned int i = 1; i <= limit; i*=2){
        if (n == i){
            cout << 1 << endl;
            return 0;
        }
    }
    cout << 0 << endl;
    return 0;
}