import sys
input = sys.stdin.readline

n = int(input())
clocks = []
times = []
for _ in range(n):
    a, b = input().rstrip().split()
    clocks.append(a)
    times.append(int(b))
idx = 0
rev = 0
time = 1
for _ in range(n):
    print(time, end = ' ')
    if clocks[idx] == "HOURGLASS" and times[idx] == time:
        print("NO")
    elif clocks[idx] == "HOURGLASS":
        rev = not rev
        print("NO")
    elif times[idx] == time:
        print("YES")
    else:
        print("NO")
    if rev:
        time -= 1
    else:
        time += 1
    if time == 0:
        time = 12
    elif time == 13:
        time = 1
    idx += 1