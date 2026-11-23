while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
    
    if a / b == float(a // b):
        print("multiple")
    elif b / a == float(b // a):
        print("factor")
    else:
        print("neither")