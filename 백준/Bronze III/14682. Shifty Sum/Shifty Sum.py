n = int(input())
sum = n
k = int(input())
for _ in range(k):
    n *= 10
    sum += n
print(sum)