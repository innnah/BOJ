import sys

n = int(input())
canSelect = [10, 60, 300]
if n % 10 != 0:
    print(-1)
    exit()

best = sys.maxsize
l = [0, 0, 0]
def push(time, cnt, select_btn=2):
    global canSelect, best, l
    if select_btn == -1:
        if time == 0:
            if sum(cnt) < best:
                best = sum(cnt)
                l = cnt.copy()
        return
    target = canSelect[select_btn]
    for i in range(time//target+1):
        a = cnt.copy()
        a[select_btn] = i
        push(time - target * i, a, select_btn - 1)

push(n, [0, 0, 0])
l = reversed(l)
print(*l if best != sys.maxsize else -1)