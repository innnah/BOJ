a, b, c = map(int, input().split())
if a+b==c:
    print(f"{a}+{b}={c}")
elif a-b==c:
    print(f"{a}-{b}={c}")
elif a*b==c:
    print(f"{a}*{b}={c}")
elif a==b+c:
    print(f"{a}={b}+{c}")
elif a==b-c:
    print(f"{a}={b}-{c}")
elif a==b*c:
    print(f"{a}={b}*{c}")
elif b%c == 0 and a==b//c:
    print(f"{a}={b}/{c}")
elif a%b == 0 and a//b==c:
    print(f"{a}/{b}={c}")