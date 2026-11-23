def divide(num, divider):
    if len(num) <= divider:
        return "0." + "0" * (divider - len(num)) + num
    else:
        return num[:len(num)-divider] + "." + num[len(num)-divider:]

def multi(a, b):
    am = a.find(".")
    bm = b.find(".")
    result = str(int(a[:am] + a[am+1:]) * int(b[:bm] + b[bm+1:]))

    return divide(result, len(a) - am - 1 + len(b) - bm - 1)

a, b = input().rstrip().split()
b = int(b)
result = a
for _ in range(b-1):
    result = multi(result, a)

print(result)