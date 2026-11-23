import sys
input = sys.stdin.readline # 입력이 숫자 30만개라서 빠른 입력을 사용해야 합니다.

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
dp1 = [[0] * 3 for _ in range(n)] # 최댓값을 구해줄 배열
dp2 = [[10 ** 7] * 3 for _ in range(n)] # 최솟값을 구해줄 배열. min 함수에서 0이 되지 않도록 큰 값을 설정한다.
# 처음에 가장 작을 때를 초기화해야 답을 계산할 수 있다.
dp1[0] = l[0]
dp2[0] = l[0]
# 답 계산
for i in range(1, n):
    dp1[i][0] = max(dp1[i-1][0], dp1[i-1][1]) + l[i][0]
    dp1[i][1] = max(dp1[i-1][0], dp1[i-1][1], dp1[i-1][2]) + l[i][1]
    dp1[i][2] = max(dp1[i-1][1], dp1[i-1][2]) + l[i][2]
    dp2[i][0] = min(dp2[i-1][0], dp2[i-1][1]) + l[i][0]
    dp2[i][1] = min(dp2[i-1][0], dp2[i-1][1], dp2[i-1][2]) + l[i][1]
    dp2[i][2] = min(dp2[i-1][1], dp2[i-1][2]) + l[i][2]

print(max(dp1[n-1]), min(dp2[n-1]))