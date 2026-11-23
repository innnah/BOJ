n = int(input())

def gcd(A,B):
    ListV = []
    if A > B:
        targetV = B
    else:
        targetV = A

    for i in range(1, targetV+1):
        if A%i == 0 and B %i == 0:
            ListV.append(i)

    var = max(ListV)
    return var

def lcm(A,B):
    V = gcd(A,B)
    divA = A//V
    divB = B//V
    return V * divA * divB

for _ in range(n):
    a, b = map(int, input().split())
    
    print(lcm(a, b))