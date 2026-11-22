import sys
from functools import cmp_to_key
input = sys.stdin.readline

def comp(a, b):
    if a+b > b+a: return -1
    elif a+b == b+a: return 0
    return 1
def filter_func(a):
    return len(a) == maxlen

n, m = map(int, input().split())
l = [input().rstrip() for _ in range(n)]
l.sort(key=cmp_to_key(comp))
maxlen = len(max(l, key = len))
l_maxlen = list(filter(filter_func, l))
ret = ""
flag = False
for i in range(n):
    ret += l[i]
    if l_maxlen[0] == l[i] and not flag:
        for _ in range(m-n):
            ret += l[i]
        flag = True
print(int(ret))