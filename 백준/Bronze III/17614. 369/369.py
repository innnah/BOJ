n = int(input())
cnt = 0
for i in range(1, n+1):
    si = str(i)
    cnt += si.count('3') + si.count('6') + si.count('9')
print(cnt)