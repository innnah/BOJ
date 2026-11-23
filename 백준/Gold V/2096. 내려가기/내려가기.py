import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
cache1 = [[0 for _ in range(3)] for _ in range(2)] # 최대
cache2 = [[10**6 for _ in range(3)] for _ in range(2)] # 최소

for i in range(3):
    cache1[0][i] = l[i]
    cache2[0][i] = l[i]

for i in range(1, n):
    l = list(map(int, input().split()))
    cache1[1][0] = l[0] + max(cache1[0][0], cache1[0][1])
    cache1[1][1] = l[1] + max(cache1[0][0], cache1[0][1], cache1[0][2])
    cache1[1][2] = l[2] + max(cache1[0][2], cache1[0][1])
    cache2[1][0] = l[0] + min(cache2[0][0], cache2[0][1])
    cache2[1][1] = l[1] + min(cache2[0][0], cache2[0][1], cache2[0][2])
    cache2[1][2] = l[2] + min(cache2[0][2], cache2[0][1])
    
    cache1[0] = cache1[1]
    cache1[1] = [0 for _ in range(3)]
    cache2[0] = cache2[1]
    cache2[1] = [0 for _ in range(3)]
    
print(max(cache1[0]), min(cache2[0]))