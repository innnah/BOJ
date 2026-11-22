import sys
from itertools import permutations
input = sys.stdin.readline

a, b = map(list, input().rstrip().split())
a = list(map(int, a))
b = list(map(int, b))
if len(a) > len(b):
    print(-1)
    sys.exit(0)
if len(a) < len(b):
    a.sort(reverse=True)
    a = list(map(str, a))
    print(''.join(a))
    sys.exit(0)
perms = list(permutations(a, len(a)))
perms.sort(reverse=True)
for perm in perms:
    flag = 0
    if perm[0] == 0:
        continue
    for i in range(len(a)):
        if perm[i] < b[i]:
            flag = 1
            break
        if perm[i] > b[i]:
            break
    if flag:
        print(''.join(map(str, perm)))
        break
else:
    print(-1)