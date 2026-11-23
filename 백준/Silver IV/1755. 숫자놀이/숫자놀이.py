m, n = map(int, input().split())
num_to_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
wordnum = []
pointer = 0

for num in range(m, n + 1):
    string = str(num)
    if num >= 10:
        wordnum.append([num_to_words[int(string[0])] + ' ' + num_to_words[int(string[1])], num])
    else:
        wordnum.append([num_to_words[int(string)], num])

wordnum.sort()

for _ in range((n - m + 1) // 10 + 1 if (n - m + 1) % 10 != 0 else (n - m + 1) // 10):
    for i in range(pointer, pointer + 10):
        try:
            print(wordnum[i][1], end = ' ')
        except:
            break
    print()
    pointer += 10