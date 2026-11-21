arr = [1 for _ in range(101)]
arr[98] = 0
arr[97] = 0
arr[94] = 0
arr[91] = 0
arr[89] = 0
arr[86] = 0
arr[85] = 0
arr[83] = 0
arr[82] = 0
arr[79] = 0
arr[73] = 0
arr[71] = 0
arr[67] = 0
arr[29] = 0
arr[28] = 0
arr[25] = 0
arr[13:23+1] = [0 for _ in range(11)]

n = int(input())
if arr[n]:
    print("16silver")
else:
    print("cozyyg")