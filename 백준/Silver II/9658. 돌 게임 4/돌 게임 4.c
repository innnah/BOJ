#include <unistd.h>

#define ReadInt(n) { \
    char c = *p++; \
    for (; ~c & 16; c = *p++); \
    for (; c & 16; c = *p++) n = 10 * n + (c & 15); }

__libc_start_main() {
    char r[10], w[10], *p = r; syscall(0, 0, r, 10);
    int n = 0; ReadInt(n);
    if (n % 7 == 1 || n % 7 == 3) w[0] = 'C', w[1] = 'Y';
    else w[0] = 'S', w[1] = 'K';
    syscall(1, 1, w, 2); _exit(0);
} main;