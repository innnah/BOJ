def f(a):
    if a%2: return 3*a+1
    return a//2
n = int(input())
cnt = 1
while n != 1:
    n = f(n)
    cnt += 1
print(cnt)