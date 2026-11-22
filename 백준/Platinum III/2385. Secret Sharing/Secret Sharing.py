import sys
input = sys.stdin.readline

def comp(a, b):
    return int(a+b) > int(b+a)
def sort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if comp(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input())
arr = input().rstrip().split()
sarr = []
for i in range(n):
    if arr[i][0] != "0":
        sarr.append(arr[i])
if len(sarr) == 0:
    print("INVALID")
    sys.exit(0)
res = 10**1000
for i in range(len(sarr)):
    cand = sarr[i]
    for j in range(len(arr)):
        if arr[j] == cand:
            arr.pop(j)
            break
    sort(arr)
    res = min(res, int(cand+''.join(arr)))
    arr.append(cand)
print(res)