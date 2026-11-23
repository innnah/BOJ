no1 = {}
no2 = {}
for i in range(97, 123):
    no1[chr(i)] = i-96
for i in range(65, 91):
    no2[chr(i)] = i-38

no = {**no1, **no2}

s = input().rstrip()
num = 0
for i in s:
    num += no[i]

for i in range(2, num):
    if num % i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")