n = bin(int(input()) + 1)[2:]
binary = n[1:]
ret = ""
for x in binary:
    if x == "0":
        ret += "4"
    else:
        ret += "7"
        
print(int(ret))