string = input().lower()
chars = [0] * 26

for x in string:
    chars[ord(x) - 97] += 1

if chars.count(max(chars)) > 1:
    print("?")
else:
    print(chr(chars.index(max(chars)) + 97).upper())