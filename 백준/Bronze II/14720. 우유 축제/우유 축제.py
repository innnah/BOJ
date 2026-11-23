n = int(input())
l = list(map(int, input().split()))
cnt = 0
milk = 0
for i in l:
    if i == milk:
        cnt += 1
        milk = (milk + 1) % 3
print(cnt)