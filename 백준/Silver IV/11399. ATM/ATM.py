n = int(input())
a = list(map(int, input().split()))

timelist = []

a.sort()

time = 0

for i in a:
    time += i
    timelist.append(time)

print(sum(timelist))