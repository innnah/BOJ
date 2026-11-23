import sys
input = sys.stdin.readline

# 입력 후 정렬. 크레인의 무게 제한과 박스의 무게를 내림차순 정렬한다.
n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

# 예외 : 무게 제한이 가장 큰 크레인도 가장 무거운 박스를 옮길 수 없으면 -1 출력.
if cranes[0] < boxes[0]:
    print(-1)
    sys.exit(0)

# 박스를 옮기는 작업을 한다. 최악의 경우 O(n²m²).
cnt = 0 # 초
while boxes:
    cnt += 1
    idx = 0 # 판단할 인덱스
    for i in range(n):
        while idx < len(boxes):
            if cranes[i] >= boxes[idx]:
                del boxes[idx]
                break
            else:
                idx += 1

print(cnt) # 걸린 시간을 출력한다.