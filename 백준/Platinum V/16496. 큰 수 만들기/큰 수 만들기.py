import sys
from functools import cmp_to_key
input = sys.stdin.readline

def cmp(x, y):
    if x+y > y+x:
        return -1
    if x+y == y+x:
        return 0
    return 1

n = int(input())
l = input().rstrip().split()
l.sort(key = cmp_to_key(cmp))
print(int(''.join(l)))