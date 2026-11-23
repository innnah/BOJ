import sys
input = sys.stdin.readline

n = int(input())
k = min(int(input()), n)
sensors = list(map(int, input().split()))
sensors.sort()

gaps = []
sortedGaps = []
willSeparate = [0 for _ in range(n)]
for i in range(1, n):
    gaps.append(sensors[i] - sensors[i-1])
    sortedGaps.append((sensors[i] - sensors[i-1], i))

sortedGaps.sort(reverse=True)
for i in range(k-1):
    willSeparate[sortedGaps[i][1]] = 1

ret = 0
for i in range(n-1):
    if not willSeparate[i+1]:
        ret += gaps[i]

print(ret)