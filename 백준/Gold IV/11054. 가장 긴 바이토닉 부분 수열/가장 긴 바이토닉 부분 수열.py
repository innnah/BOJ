import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
reversed_l = l[::-1]
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reversed_l[i] > reversed_l[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

decrease.reverse()
m = -1
for i in range(n):
    m = max(m, increase[i] + decrease[i] - 1)
print(m)