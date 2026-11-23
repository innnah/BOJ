n = int(input())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(n):
    if l2[i] == 0:
        sum2 += l[i]
    sum1 += l[i]
print(sum1)
print(sum2)