import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s3 = (s1 - s2) | (s2 - s1)
print(len(s3))