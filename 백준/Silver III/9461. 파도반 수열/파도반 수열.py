a = [1,1,1] + [0 for _ in range(97)]

for i in range(int(input())):
    n = int(input())
    for i in range(3, n):
        a[i] = a[i-2] + a[i-3]
    print(a[n-1])