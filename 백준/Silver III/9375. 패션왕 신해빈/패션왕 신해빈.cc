#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> hash;
    for (auto& a : clothes) {
        if (hash.find(a[1]) != hash.end()) hash[a[1]] += 1;
        else hash[a[1]] = 2;
    }

    for (auto i = hash.begin(); i != hash.end(); i++) answer *= i->second;

    return answer - 1;
}

int main() {
    int n, c;
    cin >> c;
    for (int i = 0; i < c; ++i) {
        vector<vector<string>> clothes;
        cin >> n;
        for (int j = 0; j < n; ++j) {
            string a, b;
            vector<string> tmp;
            cin >> a >> b;
            tmp.push_back(a); tmp.push_back(b);
            clothes.push_back(tmp);
        }
        cout << solution(clothes) << endl;
    }
    return 0;
}