import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, str(n)))
ans = [0 for _ in range(10)]

for i in range(1, arr[0]+1):
    if i != arr[0]:
        ans[i] += 10**(len(arr)-1)
    else:
        ans[i] += n%(10**(len(arr)-1)) + 1

for i in range(1, len(arr)):
    for j in range(1, 10):
        if j < arr[i]:
            ans[j] += (n//(10**(len(arr)-i))+1) * (10**(len(arr)-i-1))
        elif j == arr[i]:
            ans[j] += n//(10**(len(arr)-i)) * (10**(len(arr)-i-1)) + n%(10**(len(arr)-i-1)) + 1
        else:
            ans[j] += n//(10**(len(arr)-i)) * (10**(len(arr)-i-1))
    if arr[i] != 0:
        ans[0] += n//(10**(len(arr)-i)) * (10**(len(arr)-i-1))
    else:
        ans[0] += (n//(10**(len(arr)-i))-1) * (10**(len(arr)-i-1)) + n%(10**(len(arr)-i-1)) + 1

print(*ans)