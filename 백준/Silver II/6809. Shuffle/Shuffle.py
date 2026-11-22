import sys
input = sys.stdin.readline

arr = {chr(i+65) : input().rstrip() for i in range(26)}
arr['_'] = input().rstrip()
n = int(input())
s = input().rstrip()
d = {}
for i in range(65, 65+26):
    cnt = 1
    c = chr(i)
    cur = c
    while arr[cur] != c:
        cnt += 1
        cur = arr[cur]
    d[c] = cnt
cnt = 1
c = '_'
cur = c
while arr[cur] != c:
    cnt += 1
    cur = arr[cur]
d['_'] = cnt
for i in s:
    cur = i
    for _ in range(n%d[i]):
        cur = arr[cur]
    print(cur, end = '')