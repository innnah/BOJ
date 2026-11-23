n = int(input())
while 1:
    a = input()
    if a == "=":
        print(n)
        break
    b = input()
    n = int(eval(str(n)+a+b))