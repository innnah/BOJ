n, w, l = map(int, input().split())
truck_weights = list(map(int, input().split()))
queue = []
times = []
cnt = 0

while len(truck_weights) > 0 or len(queue) > 0:
    for i in range(len(times)):
        times[i] += 1
    if len(times) > 0:
        if times[0] >= w:
            del queue[0]
            del times[0]
    if len(truck_weights) > 0:
        if sum(queue) + truck_weights[0] <= l and len(queue) < w:
            queue.append(truck_weights[0])
            del truck_weights[0]
            times.append(0)
    cnt += 1

print(cnt)