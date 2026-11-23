days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = "No", "No"
    if 0 <= a < 24 and 0 <= b < 60:
        c = "Yes"
    if 1 <= a <= 12 and 1 <= b <= days[a]:
        d = "Yes"
    print(c, d)