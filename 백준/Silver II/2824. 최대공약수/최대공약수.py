def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

n = int(input())
numlist1 = list(map(int, input().split()))
m = int(input())
numlist2 = list(map(int, input().split()))

a = 1
b = 1
for x in numlist1:
    a *= x
for x in numlist2:
    b *= x

ret = str(gcd(a, b))
if len(ret) > 9:
    print(ret[len(ret) - 9:])
else:
    print(ret)