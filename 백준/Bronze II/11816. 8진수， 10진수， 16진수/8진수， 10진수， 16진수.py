s = input().rstrip()
if s[0] == "0":
    if s[1] == "x": print(int(s, 16))
    else: print(int(s[0]+"o"+s[1:], 8))
else: print(int(s))