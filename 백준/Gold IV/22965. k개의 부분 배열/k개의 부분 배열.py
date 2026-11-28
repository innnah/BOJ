n = int(input())
arr = list(map(int, input().split()))
a = [arr[0]]
b = []
flag = 0
for i in range(1, n):
    if not flag:
        if arr[i] > a[-1]:
            a.append(arr[i])
        else:
            b.append(arr[i])
            flag = 1
    else:
        if arr[i] > b[-1]:
            b.append(arr[i])
        else:
            print(3)
            exit(0)
if flag == 0:
    print(1)
    exit(0)
if min(a) > max(b):
    print(2)
else:
    print(3)