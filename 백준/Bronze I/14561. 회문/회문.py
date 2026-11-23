import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
    
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    converted = convert(a, b)
    if converted[::-1] == converted:
        print(1)
    else:
        print(0)