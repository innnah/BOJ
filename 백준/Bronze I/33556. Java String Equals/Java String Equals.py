import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
if a == 'null':
    print("NullPointerException")
    print("NullPointerException")
else:
    if b == 'null':
        print("false")
        print("false")
    else:
        if a == b:
            print('true')
        else:
            print('false')
        if a.lower() == b.lower():
            print('true')
        else:
            print('false')