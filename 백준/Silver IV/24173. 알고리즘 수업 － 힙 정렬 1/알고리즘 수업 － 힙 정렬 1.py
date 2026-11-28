def hf(k, s):
    global cnt
    left, right = 2*k, 2*k + 1
    if right <= s:
        if arr[left] < arr[right]: smaller = left
        else: smaller = right
    elif left <= s: smaller = left
    else: return
    if arr[smaller] < arr[k]:
        arr[k], arr[smaller] = arr[smaller], arr[k]
        cnt += 1
        if cnt == m:
            print(min(arr[k], arr[smaller]), max(arr[k], arr[smaller]))
            exit(0)
        hf(smaller, s)

cnt = 0
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, -1)
for i in range(n//2, 0, -1):
    hf(i, n)
for i in range(n, 1, -1):
    cnt += 1
    if cnt == m:
        print(min(arr[1], arr[i]), max(arr[i], arr[1]))
        exit(0)
    arr[1], arr[i] = arr[i], arr[1]
    hf(1, i-1)
else:
    print(-1)