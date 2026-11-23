import sys
input = sys.stdin.readline
n = int(input())
idx = 0
num = 1
while idx < n:
    idx += len(str(num))
    num += 1
num -= 1
num = str(num)
print(num[len(num) - (idx - n) - 1])