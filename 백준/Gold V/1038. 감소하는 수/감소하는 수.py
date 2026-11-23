n = int(input())

def solve(n):
    cnt = 0
    num = 1
    while True:
        strnum = str(num)
        flags = True
        if len(strnum) == 1:
            pass
        else:
            for i in range(1, len(strnum)):
                if strnum[i-1] <= strnum[i]:
                    start = strnum[:i-1]
                    mid = str(int(strnum[i-1]) + 1)
                    end = '0' + strnum[i+1:]
                    num = int(start + mid + end)
                    flags = False
                    break
        
        if flags:
            cnt += 1
            if cnt == n:
                return num
            num += 1

if n == 0:
    print(0)
elif n > 1022:
    print(-1)
else:
    print(solve(n))