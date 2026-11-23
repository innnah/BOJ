def match(word):
    nums = ["" for _ in range(n)]
    for i in range(maxLen):
        for j in range(n):
            nums[j] += str(int(words[j][i] == word))
    return sum(map(int, nums))

n = int(input())
words = [input() for _ in range(n)]
nums = ["" for _ in range(n)]
kind_words = set()
l = []
matched = {}
maxLen = 0
for s in words:
    maxLen = max(len(s), maxLen)
for i in range(n):
    words[i] = "0"*(maxLen-len(words[i]))+words[i]
for i in range(maxLen):
    for j in range(n):
        if words[j][i] != "0":
            kind_words.add(words[j][i])

for i in kind_words:
    l.append((match(i), i))
l.sort(reverse=True)

willMatched = 9
for i in l:
    matched[i[1]] = willMatched
    willMatched -= 1

for i in range(maxLen):
    for j in range(n):
        if words[j][i] != "0":
            nums[j] += str(matched[words[j][i]])
print(sum(map(int, nums)))