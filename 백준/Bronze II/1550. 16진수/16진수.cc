#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int toHex(string s) {
    int power = 0;
    string nums = "0123456789ABCDEF";
    int ret = 0;
    for (int i = 0; i < s.length(); i++) {
        int n = nums.find(s[i]);
        ret += n * pow(16, power);
        power += 1;
    }
    return ret;
}

int main() {
    string s;
    cin >> s;
    reverse(s.begin(), s.end());
    int ret = toHex(s);
    cout << ret << endl;
    return 0;
}