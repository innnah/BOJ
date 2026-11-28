import sys
input = sys.stdin.readline

def init(v, s, e):
    if s == e:
        tree[v] = best[s]
        return tree[v]
    mid = (s + e) // 2
    tree[v] = min(init(v*2, s, mid), init(v*2+1, mid+1, e))
    return tree[v]
def query(v, s, e, l, r):
    if e < l or r < s: return 10**20
    if l <= s <= e <= r: return tree[v]
    mid = (s + e) // 2
    return min(query(v*2, s, mid, l, r), query(v*2+1, mid+1, e, l, r))

for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(m)]
    worst = []
    for i in range(m):
        mne, mno = 10**20, 10**20
        for j in range(k):
            if arr[i][j] % 2:
                mne = min(-arr[i][j], mne)
                mno = min(arr[i][j], mno)
            else:
                mne = min(arr[i][j], mne)
                mno = min(-arr[i][j], mno)
        worst.append([mne, mno])
    best = [0 for _ in range(m+1)]
    for i in range(m):
        best[i] = best[i-1] + max(worst[i])
    tree = [0 for _ in range(m*4+4)]
    init(1, 0, m-1)
    ans = []
    left = n
    for i in range(m):
        tmp = query(1, 0, m-1, i+1, m-1) - best[i]
        if left + worst[i][0] > 0 and left + worst[i][0] + tmp > 0:
            ans.append("Even")
            left += worst[i][0]
        elif left + worst[i][1] > 0 and left + worst[i][1] + tmp > 0:
            ans.append("Odd")
            left += worst[i][1]
        else:
            print(-1)
            break
    else:
        print(' '.join(ans))