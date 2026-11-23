#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    int x1, y1, x2, y2, x3, y3, x4, y4;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
    
    if (((x3 < x1 && x1 < x4) || (x1 < x3 && x3 < x2)) && !(y1 >= y4 || y3 >= y2)) { cout << "FACE"; return 0; }
    if (((y3 < y1 && y1 < y4) || (y1 < y3 && y3 < y2)) && !(x1 >= x4 || x3 >= x2)) { cout << "FACE"; return 0; }
    
    if ((x1 == x4 || x3 == x2) && !(y1 >= y4 || y3 >= y2)) { cout << "LINE"; return 0; }
    if ((y1 == y4 || y3 == y2) && !(x1 >= x4 || x3 >= x2)) { cout << "LINE"; return 0; }
    
    if ((x1 == x4 || x3 == x2) && !(y1 > y4 || y3 > y2)) { cout << "POINT"; return 0; }
    if ((y1 == y4 || y3 == y2) && !(x1 > x4 || x3 > x2)) { cout << "POINT"; return 0; }
    
    cout << "NULL";
    return 0;
}