n = int(input())
while True:
    s = int(input())
    if s == 0: break
    if s % n == 0:
        print(f"{s} is a multiple of {n}.")
    else:
        print(f"{s} is NOT a multiple of {n}.")