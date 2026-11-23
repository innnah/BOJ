import sys, math

n = int(input())
l = 1
nums = []
for i in str(n):
    if int(i) != 0:
        nums.append(i)
for i in nums:
    l = math.lcm(l, int(i))
loop = 1
while True:
    for i in range(loop):
        if (n * loop + i) % l == 0:
            print(n * loop + i)
            sys.exit(0)
    loop *= 10