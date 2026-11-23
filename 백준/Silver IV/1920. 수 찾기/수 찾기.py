def binary_search_sub(a, x, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2 # 탐색 범위의 중간 위치
    if x == a[mid]: # 발견!
        return mid
    elif x > a[mid]: # 찾는 값이 더 크면 중간을 기준으로 오른쪽 값을 대상으로 재귀 호출
        return binary_search_sub(a, x, mid + 1, end)
    else:            # 찾는 값이 더 작으면 중간을 기준으로 왼쪽 값을 대상으로 재귀 호출
        return binary_search_sub(a, x, start, mid - 1)

    return -1

def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a) - 1)

n = int(input())
numlist1 = list(map(int, input().split()))
m = int(input())
numlist2 = list(map(int, input().split()))
numlist1.sort()

for x in numlist2:
    if binary_search(numlist1, x) == -1:
        print(0)
    else:
        print(1)