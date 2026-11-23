def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
numlist = list(map(int, input().split()))
maximum = max(numlist)
minimum = min(numlist)

for i in range(n - 1):
    ret = lcm(numlist[i], numlist[i + 1])
    numlist[i + 1] = ret
    
if numlist[-1] == maximum:
    print(numlist[-1] * minimum)
else:
    print(numlist[-1])