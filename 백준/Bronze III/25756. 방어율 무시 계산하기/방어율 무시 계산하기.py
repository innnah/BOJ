n = int(input())
l = list(map(int, input().split()))
p = 1
for i in l:
    p = p * (1-i/100)
    print((1-p)*100)