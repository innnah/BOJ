#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, int> arr;

int main() {
    for (int i = 1; i < 11; i++) {
        for (int j = 1; j < 11; j++) {
            arr.insert(pair<string, int>(to_string(i) + to_string(j), i + j));
        }
    }
    string s;
    cin >> s;
    cout << arr[s] << endl;
    return 0;
}