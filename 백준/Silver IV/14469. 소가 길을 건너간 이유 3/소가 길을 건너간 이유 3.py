n = int(input())
numlist = [list(map(int, input().split())) for _ in range(n)]
numlist.sort()
times = 0

for i in range(n):
    if times > 0:
        times += sum(numlist[i])
    else:
        times = sum(numlist[i])
    try:
        times = times - numlist[i + 1][0]
    except:
        break

print(times)