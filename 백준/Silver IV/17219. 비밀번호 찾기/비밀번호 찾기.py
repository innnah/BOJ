import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
passwords = dict([input().split() for _ in range(n)])
toFind = [input().rstrip() for _ in range(m)]

for x in toFind:
    print(passwords[x] + "\n")