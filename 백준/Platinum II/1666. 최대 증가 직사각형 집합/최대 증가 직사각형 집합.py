import sys
input = sys.stdin.readline

def query(le, ri, v, s, e):
    if le > e or ri < s: return 0
    if le <= s <= e <= ri: return tree[v]
    mid = (s + e) // 2
    return max(query(le, ri, v*2, s, mid), query(le, ri, v*2+1, mid+1, e))
def update(idx, val, v, s, e):
    if idx < s or idx > e: return tree[v]
    if s == e: 
        tree[v] = max(tree[v], val)
        return tree[v]
    mid = (s + e) // 2
    tree[v] = max(update(idx, val, v*2, s, mid), update(idx, val, v*2+1, mid+1, e))
    return tree[v]

n = int(input())
arr = [list(map(int, input().split())) + [i] for i in range(n)]
arr.sort()
earr = sorted(arr, key=lambda x: -x[2])
d = [0 for _ in range(n)]
for i in range(n):
    d[earr[i][4]] = i

tree = [0 for _ in range(262145)]
for i in range(n):
    #print(earr)
    while earr and earr[-1][2] < arr[i][0]:
        rect = earr.pop()
        update(rect[3], rect[5], 1, 0, 100000)
    earr[d[arr[i][4]]].append(query(0, arr[i][1]-1, 1, 0, 100000) + 1)
while earr:
    rect = earr.pop()
    update(rect[3], rect[5], 1, 0, 100000)
print(query(0, 100000, 1, 0, 100000))