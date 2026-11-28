import sys, bisect
input = sys.stdin.readline

def init(v, s, e):
    if s == e:
        tree_m[v] = arr2[s]
        return
    mid = (s + e) // 2
    init(v*2, s, mid)
    init(v*2+1, mid+1, e)
    tree_m[v] = max(tree_m[v*2], tree_m[v*2+1])

def max_query(v, s, e, l, r):
    if r < s or e < l: return -1
    if l <= s <= e <= r: return tree_m[v]
    mid = (s + e) // 2
    left = max_query(v*2, s, mid, l, r)
    right = max_query(v*2+1, mid+1, e, l, r)
    return max(left, right)

n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [1]
for i in range(1, n):
    if arr[i] == arr[i-1]:
        arr2[-1] += 1
    else:
        arr2.append(1)

tree_m = [0 for _ in range(262144)]
psum = [0 for _ in range(len(arr2)+1)]
for i in range(len(arr2)):
    psum[i] = psum[i-1] + arr2[i]
psum.pop()
init(1, 0, len(arr2)-1)
for _ in range(q):
    a, b = map(int, input().split())
    x, y = bisect.bisect_left(psum, a), bisect.bisect_left(psum, b)
    if x == y: print(b-a+1)
    elif y-x == 1:
        left, right = psum[x]-a+1, b-psum[x]
        print(max(left, right))
    else:
        left = psum[x]-a+1
        right = b-psum[y-1]
        mid = max_query(1, 0, len(arr2)-1, x+1, y-1)
        print(max(left, right, mid))