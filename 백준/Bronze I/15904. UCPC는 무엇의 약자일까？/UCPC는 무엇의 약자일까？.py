s = input()
target = ["U", "C", "P", "C"]
check = True
for i in range(4):
    if target[i] in s:
        check = True
        s = s[s.find(target[i])+1:]
    else:
        check = False
        break

print("I love UCPC" if check else "I hate UCPC")