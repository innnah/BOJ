import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = [input().rstrip().split() for _ in range(n)]
arr2 = [input().rstrip().split() for _ in range(m)]
arr1 = [[int(i[0]), i[1]] for i in arr1]
arr2 = [[int(i[0]), i[1]] for i in arr2]

pos1 = [0 for _ in range(1000001)]
pos2 = [0 for _ in range(1000001)]
pos = 0
t = 0
for i in arr1:
    if i[1] == 'L':
        for _ in range(i[0]):
            t += 1
            pos -= 1
            pos1[t] = pos
    else:
        for _ in range(i[0]):
            t += 1
            pos += 1
            pos1[t] = pos
for i in range(t, 1000001):
    pos1[i] = pos
pos = 0
t = 0
for i in arr2:
    if i[1] == 'L':
        for _ in range(i[0]):
            t += 1
            pos -= 1
            pos2[t] = pos
    else:
        for _ in range(i[0]):
            t += 1
            pos += 1
            pos2[t] = pos
for i in range(t, 1000001):
    pos2[i] = pos
moo = 0
for i in range(1000000):
    if pos1[i] > pos2[i]:
        if pos1[i+1] <= pos2[i+1]:
            moo += 1
    elif pos1[i] < pos2[i]:
        if pos1[i+1] >= pos2[i+1]:
            moo += 1

print(moo)