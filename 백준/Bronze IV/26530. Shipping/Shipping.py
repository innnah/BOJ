for _ in range(int(input())):
    things = int(input())
    answer = 0
    for _ in range(things):
        _, count, price = input().split()
        answer += float(count) * float(price)
    print("$%0.2f" % answer)