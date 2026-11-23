from fractions import Fraction
a, b = map(int, input().split())
frac = Fraction(a, b)
ret = str(1 - frac)
idx = ret.find("/")
retA = ret[:idx]
retB = ret[idx+1:]
print(retA, retB)