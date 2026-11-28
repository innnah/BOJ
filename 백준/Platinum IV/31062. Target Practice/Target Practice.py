import sys
input = sys.stdin.readline

def add(v):
    global cand
    t = d.get(v)
    if t != None:
        cnt[t] += 1
        if cnt[t] == 1:
            cand += 1
def sub(v):
    global cand
    t = d.get(v)
    if t != None:
        cnt[t] -= 1
        if cnt[t] == 0:
            cand -= 1

m, n = map(int, input().split())
tmp = sorted(map(int, input().split()))
d = {tmp[i] : i for i in range(m)}
dir = list(input().rstrip())

arr = [0]
for i in range(n):
    if dir[i] == 'L': arr.append(arr[-1]-1)
    elif dir[i] == 'R': arr.append(arr[-1]+1)
    else: arr.append(arr[-1])
arr.pop(0)

no_move_cnt = [0 for _ in range(m)]
for i in range(n):
    if dir[i] == 'F':
        v = d.get(arr[i])
        if v != None: no_move_cnt[v] += 1
no_move = 0
for i in range(m):
    if no_move_cnt[i]: no_move += 1

ans = no_move
p, cand, cnt = n-1, no_move, no_move_cnt.copy()
for i in range(n-1, -1, -1):
    if dir[i] == "L":
        for j in range(i+1, p+1):
            if dir[j] == 'F':
                sub(arr[j])
                add(arr[j]+2)
        ans = max(ans, cand)
        p = i-1

p, cand, cnt = n-1, no_move, no_move_cnt.copy()
for i in range(n-1, -1, -1):
    if dir[i] == "L":
        add(arr[i]+1)
        for j in range(i+1, p+1):
            if dir[j] == 'F':
                sub(arr[j])
                add(arr[j]+1)
        ans = max(ans, cand)
        p = i-1
        sub(arr[i]+1)
    elif dir[i] == 'F':
        sub(arr[i])
        for j in range(i+1, p+1):
            if dir[j] == 'F':
                sub(arr[j])
                add(arr[j]+1)
        ans = max(ans, cand)
        p = i-1
        add(arr[i]+1)

p, cand, cnt = n-1, no_move, no_move_cnt.copy()
for i in range(n-1, -1, -1):
    if dir[i] == "R":
        for j in range(i+1, p+1):
            if dir[j] == 'F':
                sub(arr[j])
                add(arr[j]-2)
        ans = max(ans, cand)
        p = i-1

p, cand, cnt = n-1, no_move, no_move_cnt.copy()
for i in range(n-1, -1, -1):
    if dir[i] == "R":
        add(arr[i]-1)
        for j in range(i+1, p+1):
            if dir[j] == 'F':
                sub(arr[j])
                add(arr[j]-1)
        ans = max(ans, cand)
        p = i-1
        sub(arr[i]-1)
    elif dir[i] == 'F':
        sub(arr[i])
        for j in range(i+1, p+1):
            if dir[j] == 'F':
                sub(arr[j])
                add(arr[j]-1)
        ans = max(ans, cand)
        p = i-1
        add(arr[i]-1)

print(ans)