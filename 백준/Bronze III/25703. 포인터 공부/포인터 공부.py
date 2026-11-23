n = int(input())
print("int a;")
for i in range(n):
    if i == 0:
        print("int *ptr = &a;")
    else:
        print("int " + "*"*(i+1) + "ptr" + str(i+1) + " = &" + "ptr" + (str(i) if i != 1 else "") + ";")