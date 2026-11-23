n = int(input())
numlist = list(map(int, input().split()))
words = list(input())
numlist.sort()
words.sort()

for x in range(n):
    if words[x].isupper():
        if not ord(words[x]) - 64 == numlist[x]:
            print("n")
            break
    elif words[x].islower():
        if not ord(words[x]) - 70 ==  numlist[x]:
            print("n")
            break
    else:
        if not 0 == numlist[x]:
            print("n")
            break
else:
    print("y")