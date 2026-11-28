import sys
input = sys.stdin.readline

while 1:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    mn = 10**20
    ans = [0, 0]
    for i in range(n):
        a, b = map(int, input().split())
        if a <= m and (b/a < mn or (b/a == mn and ans[0] < a)):
            mn = b/a
            ans = [a, b]
    if ans == [0, 0]:
        print("No suitable tickets offered")
    else:
        print(f"Buy {ans[0]} tickets for ${ans[1]}")