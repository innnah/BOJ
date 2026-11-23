cnt = 0

for _ in range(int(input())):
    word = input().rstrip()
    if len(word) == 1:
        cnt += 1
        continue
    if len(list(set(word))) == len(list(word)):
        cnt += 1
        continue
        
    freq = word[0]
    freqs = []
    for x in word:
        if freq != x:
            freqs.append(freq)
            freq = x
            if freq in freqs:
                break
    else:
        cnt += 1
                
print(cnt)