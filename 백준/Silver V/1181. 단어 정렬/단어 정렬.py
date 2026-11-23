n = int(input())
words = [input().rstrip() for _ in range(n)]
words = list(set(words))

for i in range(len(words)):
    s = words[i]
    words[i] = [len(s), s]

words.sort()

for x in words:
    print(x[1])