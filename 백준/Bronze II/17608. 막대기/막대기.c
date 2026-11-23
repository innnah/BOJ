#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int heights[100000];

int main() {
	int n;
	scanf("%d", &n);
	for (int i = n-1; i >= 0; i--) {
		scanf("%d", &heights[i]);
	}
	int cnt = 1;
	int maximum = heights[0];
	for (int i = 0; i < n; i++) {
		if (maximum < heights[i]) {
			maximum = heights[i];
			cnt++;
		}
	}
	printf("%d\n", cnt);
}