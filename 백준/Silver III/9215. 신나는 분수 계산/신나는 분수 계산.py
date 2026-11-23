import fractions

i = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    fracs = []
    s = ""
    for _ in range(n):
        s = input().rstrip().split(",")
        frac = None
        if len(s) == 2:
            frac = fractions.Fraction(str(int(s[-1][s[-1].find("/") + 1:]) * int(s[0]) + int(s[-1][:s[-1].find("/")])) + "/" + s[-1][-1])
        else:
            frac = fractions.Fraction(s[0])

        fracs.append(frac)

    total = str(sum(fracs))
    index = total.find("/")
    result = ""
    if index != - 1:
        divider = int(total[index + 1:])
        divided = int(total[:index])
        
        if divided > divider:
            result += str(divided // divider) + ","
            result += str(divided % divider) + "/" + str(divider)
        else:
            result = str(total)
    else:
        result = str(total)

    print(f"Test {i}: {result}")
    i += 1