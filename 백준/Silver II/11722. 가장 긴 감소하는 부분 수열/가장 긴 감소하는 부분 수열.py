cache = [-1 for _ in range(1001)]
def lis(start):
    if start == len(a)-1: 
        return 1

    ret = cache[start]
    if ret != -1: return ret

    ret = 1
    for i in range(start+1, len(a)):
        if a[start] > a[i]:
            ret = max(ret, lis(i)+1)
    cache[start] = ret
    return ret

n = int(input())
a = list(map(int, input().split()))
maxLen = -1
for i in range(n):
    maxLen = max(maxLen, lis(i))
print(maxLen)