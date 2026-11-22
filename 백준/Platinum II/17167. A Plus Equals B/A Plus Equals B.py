import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0
steps = []
while a != b:
    cnt += 1
    if a % 2 == 0:
        a //= 2
        steps.append("B+=B")
    elif b % 2 == 0:
        b //= 2
        steps.append("A+=A")
    else:
        if a > b:
            a += b
            steps.append("A+=B")
        else:
            b += a
            steps.append("B+=A")
print(cnt)
print("\n".join(steps))