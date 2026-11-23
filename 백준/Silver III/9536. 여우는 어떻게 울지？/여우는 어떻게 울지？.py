for _ in range(int(input())):
    words = input().rstrip().split()
    others = []
    while True:
        word = input().rstrip().split()[-1]
        if word == "say?":
            break
        others.append(word)
        
    for x in others:
        for _ in range(words.count(x)):
            words.remove(x)
            
    for x in words:
        print(x, end = ' ')