import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
l = list(permutations([i for i in range(10)], n+1))
a = input().rstrip().split()
mini, maxi = 999999999999, 0
for p in l:
    for i in range(n):
        if a[i] == '<':
            if p[i] >= p[i+1]:
                break
        else:
            if p[i] <= p[i+1]:
                break
    else:
        num = 0
        for i in range(n+1):
            num *= 10
            num += p[i]
        maxi = max(maxi, num)
        mini = min(mini, num)
maxi = str(maxi)
mini = str(mini)
print('0'*(n-len(maxi)+1) + maxi)
print('0'*(n-len(mini)+1) + mini)