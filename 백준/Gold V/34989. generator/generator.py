import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
if n%2 and arr[n//2] == 0:
    arr[n//2] = 1
demand = input().rstrip()
if demand == 'no':
    num = []
    for i in range(1, 2001):
        if i not in arr:
            num.append(i)
    idx = 0
    for i in range(n//2):
        if arr[i] == 0:
            arr[i] = num[idx]
            idx += 1
            break
        if arr[n-i-1] == 0:
            arr[n-i-1] = num[idx]
            idx += 1
            break
    for i in range(n):
        if arr[i] == 0:
            arr[i] = num[idx]
            idx += 1
    print(' '.join(map(str, arr)))
else:
    for i in range(1, n//2+1):
        if arr[:i] == arr[-i:] and 0 not in arr[:i]:
            break
        flag = 0
        for j in range(i):
            if arr[j] != 0 and arr[-i+j] != 0 and arr[j] != arr[-i+j]:
                flag = 1
                break
        if flag: continue
        for j in range(i):
            if arr[j] == 0 and arr[-i+j] != 0:
                arr[j] = arr[-i+j]
            elif arr[j] != 0 and arr[-i+j] == 0:
                arr[-i+j] = arr[j]
            elif arr[j] == 0 and arr[-i+j] == 0:
                arr[j] = arr[-i+j] = 1
    for i in range(n):
        if arr[i] == 0:
            arr[i] = 1
    print(' '.join(map(str, arr)))