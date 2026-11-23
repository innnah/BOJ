//#pragma GCC optimize("O3")
//#pragma GCC target("arch=skylake")

#include <unistd.h>
#include <stdio.h>
#include <string.h>

char IN[1200000] = { 0 };
int CNT_INFO[10001] = { 0 };
int C;

int main(void)
{
	char *p;
	int sz, remain;
	int num;
	int f, c, k, j;
	char *s, tmp[7];
	FILE *fp;

	read(0, IN, sizeof(IN));
	p = IN;
	sz = sizeof(IN);

	for (C = 0; *p++ >= 48; ) {
		C = C * 10 + (*(p - 1) - 48);
	}

	while (C--) {
		remain = IN + sz - p;
		if (remain < 6) {
			memcpy(IN, p, remain);
			read(0, IN + remain, sz - remain);
			p = IN;
		}
		for (num = 0; *p++ >= 48; ) {
			num = num * 10 + (*(p - 1) - 48);
		}
		CNT_INFO[num]++;
	}

	p = IN;

	for (num = 1; num <= 10000; num++) {
		if (CNT_INFO[num]) {
		check_1:
			tmp[6] = '\n';
			for (k = num, j = 0; k > 0; k /= 10, j++) {
				tmp[5-j] = (k % 10) + '0';
			}
			j++;
			memcpy(p, tmp + 7 - j, j);

			s = p;
			p += j;
			CNT_INFO[num]--;
			f = 1;

			while (CNT_INFO[num] > 0) {
				if (CNT_INFO[num] >= f) {
					c = f;
				}
				else {
					c = CNT_INFO[num];
				}

				if (IN + sz - p - 1 < j * c) {
					//*p++ = '\0';
					//printf("%s",IN);
					write(1, IN, p - IN);
					p = IN;
					goto check_1;
				}

				memcpy(p, s, j*c);
				p += j * c;
				CNT_INFO[num] -= c;
				f += c;
			}
		}
	}

	//*p++ = '\0';
	//printf("%s",IN);
	write(1, IN, p - IN);

	return 0;
}