s = input()
ret = ""
for i in s:
    if i.isalpha():
        if i.isupper():
            ret += chr((ord(i)-65+13) % 26 + 65)
        else:
            ret += chr((ord(i)-97+13) % 26 + 97)
    else:
        ret += i
print(ret)