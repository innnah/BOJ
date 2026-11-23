import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
s = 0
for _ in range(n):
    order = input().rstrip().split()
    if len(order) == 2: order[1] = int(order[1])
    if order[0] == 'add':
        s |= 1 << order[1]
    elif order[0] == 'remove':
        s &= ~(1 << order[1])
    elif order[0] == 'check':
        print(str(int(bool(s & (1 << order[1])))) + "\n")
    elif order[0] == 'toggle':
        s ^= 1 << order[1]
    elif order[0] == 'all':
        s = (1 << 21) - 1
    else:
        s = 0