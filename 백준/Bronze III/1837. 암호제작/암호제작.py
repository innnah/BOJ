n, k = map(int, input().split())
for i in range(2, k):
    if n % i == 0:
        print(f"BAD {i}")
        break
else:
    print("GOOD")