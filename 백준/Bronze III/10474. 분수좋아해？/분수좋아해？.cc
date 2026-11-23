#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

using namespace std;

int main() {
    int a, b;
    while (true) {
        scanf("%d %d", &a, &b);
        if (a == 0 && b == 0) break;
        printf("%d ", a / b);
        printf("%d / %d\n", a % b, b);
    }
    return 0;
}