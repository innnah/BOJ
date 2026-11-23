n, k = map(int, input().split())
numlist = list(map(int, input().split()))
totals = []
for i in range(n-k+1):
    totals.append(sum(numlist[i:i+k]))
        
print(max(totals))