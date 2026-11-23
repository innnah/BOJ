from bisect import bisect_left

n = int(input())
l = list(map(int, input().split()))

L = [l[0]]
for i in l:
    if L[-1] < i:
        L.append(i)
    else:
        lower_bound = bisect_left(L, i)
        L[lower_bound] = i
        
print(n-len(L))