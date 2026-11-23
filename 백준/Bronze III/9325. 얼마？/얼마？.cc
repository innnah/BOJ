#include<stdio.h>
using namespace std;
int t;
int main() {
    scanf("%d", &t);
    while (t--) {
        int price, options;
        scanf("%d %d", &price, &options);
        while (options--) {
            int q, p;
            scanf("%d %d", &q, &p);
            price += q * p;
        }
        printf("%d\n", price);
    }
    return 0;
}