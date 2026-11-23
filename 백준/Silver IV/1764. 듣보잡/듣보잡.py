n, m = map(int, input().split())

not_hear = [input() for _ in range(n)]
not_see = [input() for _ in range(m)]

not_hear_see = list(set(not_hear).intersection(not_see))
not_hear_see.sort()

print(len(not_hear_see))
for x in not_hear_see:
    print(x.rstrip())