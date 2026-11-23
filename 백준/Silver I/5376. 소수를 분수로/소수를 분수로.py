import fractions

t = int(input())

for _ in range(t):
    s = input()

    if s.find('(') == -1:
        frac = fractions.Fraction(s)
        print(frac)
    else:
        dotIndex = s.find('.')
        start = s.find('(')
        end = s.find(')')
        startNum = s[dotIndex + 1:start]
        recurNum = s[start + 1: end]
        
        if len(startNum) != 0:
            tmp = str(int(startNum + recurNum) - int(startNum)) + '/' + len(recurNum) * '9' + len(startNum) * '0'
        else:
            tmp = recurNum + '/' + len(recurNum) * '9'
        frac = fractions.Fraction(tmp)
        print(frac)