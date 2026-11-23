n = int(input())
for i in range(1, n+1):
    strings = input().rstrip().split()
    print(f"Case #{i}: ", end = '')
    for s in strings[::-1]:
        print(s, end = ' ')
    print()