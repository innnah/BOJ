n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
for r in range(n):
    for i in range(m//2):
        if arr[r][i] != '.':
            arr[r][m-i-1] = arr[r][i]
        if arr[r][m-i-1] != '.':
            arr[r][i] = arr[r][m-i-1]
    print(''.join(arr[r]))