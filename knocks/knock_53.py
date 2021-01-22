nums: list = [1, 2, 4, 3, 2, 1, 5, 1]
# counter = {}
# for num in set(nums):
#     counter[num] = nums.count(num)
# print(counter)
# {1: 3, 2: 2, 3: 1, 4: 1, 5: 1}

counter = {}
for num in nums:
    counter[num] = counter.get(num, 0) + 1
print(counter)