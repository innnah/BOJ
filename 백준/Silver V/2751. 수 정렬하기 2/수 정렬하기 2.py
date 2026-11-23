import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

numlist = [int(input()) for _ in range(n)]

numlist.sort()

for x in numlist:
    print(f"{x}\n")