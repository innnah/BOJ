from datetime import *

for _ in range(int(input())):
    a, b = map(int, input().split())
    d = list(map(int, str(datetime(a, b, b) - timedelta(days=b))[:-9].split("-")))
    print(d[0], d[1], d[2])