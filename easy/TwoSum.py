def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i

# Example input
nums = [3,3]
target = 6

result = twoSum(nums, target)
print(result)