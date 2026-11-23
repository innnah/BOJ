n = int(input())
print(2**n-1)

def solve(circle, to, where):
    if circle == 1:
        print(*[where,to])
        return
    
    left = -1
    if [to, where] == [1,3] or [to, where] == [3,1]:
        left = 2
    elif [to, where] == [1,2] or [to, where] == [2,1]:
        left = 3
    else:
        left = 1

    solve(circle-1, left, where)
    print(*[where,to])
    solve(circle-1, to, left)

if n <= 20:
    solve(n, 3, 1)