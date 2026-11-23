#include <bits/stdc++.h>
#include <cstdio>
#define ll long long

using namespace std;

const int N = 2000001;
int tree[N*4+1];
int query(int val, int v=1, int s=0, int e=N-1) {
    if (s == e) return s;
    int mid = (s+e)/2;
    if (tree[v*2] < val) return query(val-tree[v*2], v*2+1, mid+1, e);
    return query(val, v*2, s, mid);
}
int update(int idx, int val, int v=1, int s=0, int e=N-1) {
    if (idx < s || idx > e) return tree[v];
    if (s == e) {
        tree[v] += val;
        return tree[v];
    }
    int mid = (s+e)/2;
    return tree[v] = update(idx, val, v*2, s, mid) + update(idx, val, v*2+1, mid+1, e);
}
int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int a, b;
        scanf("%d %d", &a, &b);
        if (a-1) {
            int tmp = query(b);
            printf("%d\n", tmp);
            update(tmp, -1);
        }
        else {
            update(b, 1);
        }
    }
    return 0;
}