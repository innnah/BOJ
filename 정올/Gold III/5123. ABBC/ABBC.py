import sys
from collections import deque
input = sys.stdin.readline

s = input().rstrip()
aq, bq = deque(), deque()
ret = 0
for i in range(len(s)):
    if s[i] == 'A':
        aq.append(i)
    elif s[i] == 'B':
        bq.append(i)
    else:
        if bq and bq[0] < i:
            bq.popleft()
            ret += 1
while aq and bq:
    if aq[0] < bq[0]:
        aq.popleft()
        bq.popleft()
        ret += 1
    else:
        bq.popleft()
print(ret)