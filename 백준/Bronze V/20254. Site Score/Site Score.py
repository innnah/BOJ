l = list(map(int, input().split()))
mul = [56, 24, 14, 6]
sum = 0
for i in range(4):
    sum += l[i] * mul[i]
print(sum)