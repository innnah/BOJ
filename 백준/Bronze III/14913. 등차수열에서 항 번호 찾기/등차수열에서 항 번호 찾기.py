n, m, k = map(int, input().split())
if n%m != k%m or (n<k and m<=0) or (n>k and m>=0):
    print("X")
else:
    print((k-n) // m + 1)