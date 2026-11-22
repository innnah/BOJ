from collections import defaultdict
for _ in range(int(input())):
    da = defaultdict(int)
    db = defaultdict(int)
    a, b = input().split()
    for i in a:
        da[i] += 1
    for i in b:
        db[i] += 1
    print(f"{a} & {b} are " + "NOT " * (da != db) + "anagrams.")