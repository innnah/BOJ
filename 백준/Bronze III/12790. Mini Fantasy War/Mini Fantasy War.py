for _ in range(int(input())):
    arr = list(map(int, input().split()))
    for i in range(4):
        arr[i] += arr[i+4]
    arr[0] = max(1, arr[0])
    arr[1] = max(1, arr[1])
    arr[2] = max(0, arr[2])
    print(arr[0] + 5*arr[1] + 2*(arr[2]+arr[3]))