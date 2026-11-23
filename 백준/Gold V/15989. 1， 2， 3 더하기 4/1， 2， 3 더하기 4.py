import sys

input = sys.stdin.readline

k = int(input())
cache = [1 for _ in range(10001)]
for i in range(2, 10001):
    cache[i] += cache[i - 2]
for i in range(3, 10001):
    cache[i] += cache[i - 3]

for _ in range(k):
    print(cache[int(input())])