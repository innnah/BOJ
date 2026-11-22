import sys
from collections import defaultdict
input = sys.stdin.readline

s = input().rstrip()
if len(s) % 2:
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    odds = 0
    for i in d.values():
        odds += i%2
    if odds > 1:
        print("I'm Sorry Hansoo")
    else:
        l = list(d.keys())
        l.sort()
        st = ""
        ret = ""
        for i in l:
            if d[i] % 2:
                st = i
            ret += i * (d[i]//2)
        print(ret+st+ret[::-1])
else:
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    odds = 0
    for i in d.values():
        odds += i%2
    if odds > 0:
        print("I'm Sorry Hansoo")
    else:
        l = list(d.keys())
        l.sort()
        st = ""
        ret = ""
        for i in l:
            if d[i] % 2:
                st = i
            ret += i * (d[i]//2)
        print(ret+st+ret[::-1])
