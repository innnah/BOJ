nums1 = set(range(1, 10001))
nums2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    nums2.add(i)

result = sorted(nums1 - nums2)
for i in result:
    print(i)