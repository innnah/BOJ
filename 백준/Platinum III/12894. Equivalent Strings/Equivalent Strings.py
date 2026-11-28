import sys
input = sys.stdin.readline

def equivalent(p1, p2):
    if len(p1) % 2 == 1:
        return p1 == p2
    mid = len(p1) // 2
    a = equivalent(p1[:mid], p2[:mid])
    b = equivalent(p1[:mid], p2[mid:])
    k = a*2+b
    if k == 0: return 0
    elif k == 1: return equivalent(p1[mid:], p2[:mid])
    return equivalent(p1[mid:], p2[mid:])

s1 = input().rstrip()
s2 = input().rstrip()
n = len(s1)
if equivalent(s1, s2):
    print("YES")
else:
    print("NO")