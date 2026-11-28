s = input()
if len(s) <= 2:
    print("CE")
idx1 = s.find("\"")
idx2 = s.rfind("\"")
if idx1 == 0 and idx2 == len(s)-1:
    print(s[1:-1])
else:
    print("CE")