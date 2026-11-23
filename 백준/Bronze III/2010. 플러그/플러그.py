import sys
input = sys.stdin.readline
n = int(input())
sum = -n+1
for _ in range(n):
    k = int(input())
    sum += k
print(sum)