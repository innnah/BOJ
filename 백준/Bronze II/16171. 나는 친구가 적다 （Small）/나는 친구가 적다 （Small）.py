s = input()
newString = ""
sub = input()

for x in s:
    if x.isalpha():
        newString += x

if newString.find(sub) == -1:
    print(0)
else:
    print(1)