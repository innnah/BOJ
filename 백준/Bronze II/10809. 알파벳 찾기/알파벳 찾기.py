words = [-1] * 26
string = input()

for x in string:
    if words[ord(x) - 97] == -1:
        words[ord(x) - 97] = string.find(x)

for x in words:
    print(x, end = ' ')