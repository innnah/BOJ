import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip()))
if arr == [1] * n:
    print(2-(n%2))
    sys.exit(0)
arr2 = []
cnt = 0
for i in range(n):
    if arr[i] == 0:
        if cnt:
            arr2.append(cnt)
            cnt = 0
    else:
        cnt += 1
cnt2, cnt3 = 0, 0
for i in range(n):
    if arr[i] == 0: break
    cnt2 += 1
if cnt:
    cnt3 = cnt

if arr[0]: arr2.pop(0)

days = 10**20
if arr2: days = min((min(arr2)+1)//2, days)
if cnt2: days = min(cnt2, days)
if cnt3: days = min(cnt3, days)

ret = 0
for i in arr2:
    ret += (i+days*2-2)//(days*2-1)
ret += (cnt2+days*2-2)//(days*2-1)
ret += (cnt3+days*2-2)//(days*2-1)
print(ret)