#include <bits/stdc++.h>
#include <cstdio>
#define MAXN 1010101

using namespace std;

int tree[MAXN*4+1], arr[MAXN], n, m;
int makeTree(int v, int s, int e) {
    if (s == e) {
        tree[v] = arr[s];
        return tree[v];
    }
    int mid = (s+e)/2;
    return tree[v] = max(makeTree(v*2, s, mid), makeTree(v*2+1, mid+1, e));
}
int query(int l, int r, int v, int s, int e) {
    if (l > e || r < s) return 0;
    if (l <= s && e <= r) return tree[v];
    int mid = (s+e)/2;
    return max(query(l, r, v*2, s, mid), query(l, r, v*2+1, mid+1, e));
}
int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &(arr[i]));
    }
    makeTree(1, 0, n-1);
    for (int i = m-1; i < n-m+1; ++i) {
        printf("%d ", query(i-m+1, i+m-1, 1, 0, n-1));
    }
    return 0;
}