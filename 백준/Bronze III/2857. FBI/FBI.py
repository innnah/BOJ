flag = False
for i in range(5):
    s = input()
    if "FBI" in s:
        print(i+1)
        flag = True
if not flag:
    print("HE GOT AWAY!")