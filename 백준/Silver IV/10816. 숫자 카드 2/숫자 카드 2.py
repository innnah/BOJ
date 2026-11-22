import sys, bisect
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
for i in b:
    print(str(bisect.bisect(a, i) - bisect.bisect_left(a, i)) + " ")