'''
Scenario #1:
yes

Scenario #2:
no
'''
for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(f"Scenario #{i + 1}:")
    maximum = max(a, b, c)
    if maximum == a:
        if b ** 2 + c ** 2 == a ** 2:
            print("yes")
        else:
            print("no")         
    if maximum == b:
        if a ** 2 + c ** 2 == b ** 2:
            print("yes")
        else:
            print("no")
    if maximum == c:
        if a ** 2 + b ** 2 == c ** 2:
            print("yes")
        else:
            print("no")            
    print()