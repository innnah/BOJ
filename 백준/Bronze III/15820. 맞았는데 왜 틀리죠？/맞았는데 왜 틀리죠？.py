n, m = map(int, input().split())
flag1, flag2 = True, True
for _ in range(n):
    a, b = map(int, input().split())
    if a != b: flag1 = False
for _ in range(m):
    a, b = map(int, input().split())
    if a != b: flag2 = False
if flag1:
    if flag2: print("Accepted")
    else: print("Why Wrong!!!")
else:
    print("Wrong Answer")