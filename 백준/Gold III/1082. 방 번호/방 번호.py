import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
p = int(input())

minval = [100, -1]
for i in range(n):
    if minval[0] >= arr[i]:
        minval = [arr[i], i]

num = str(minval[1]) * (p // minval[0])
price = len(num) * minval[0]
for i in range(len(num)):
    for j in range(n-1, minval[1], -1):
        if price - minval[0] + arr[j] <= p:
            num = num[:i] + str(j) + num[i+1:]
            price = price - minval[0] + arr[j]
            break
    else:
        if int(num[:i+1]) == 0:
            price -= minval[0]
print(int(num))