#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

using namespace std;

int n, x, y, num, ret;
int result[30];

void getNumlists(int idx = 1) {
	if (idx > n) {
		ret += 1;
		return;
	}
	if (idx == num) getNumlists(idx + 1);
	for (int i = idx + 1; i < n * 2; i++) {
		if (!result[i] && !result[i - (idx + 1)]) {
			result[i] = result[i - (idx + 1)] = idx;
			getNumlists(idx + 1);
			result[i] = result[i - (idx + 1)] = 0;
		}
	}
}
int main() {
    scanf("%d %d %d", &n, &x, &y);
	num = y - x - 1;
	result[x-1] = result[y-1] = num;
	getNumlists();
	printf("%d", ret);
	return 0;
}