import fractions

n = int(input())
rList = list(map(int, input().split()))

for x in rList[1:]:
    frac = fractions.Fraction(rList[0], x)

    if frac == int(frac):
        print(f"{frac}/1")
        continue

    print(frac)