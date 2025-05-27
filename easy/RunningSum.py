def runningSum(nums):
    new_nums = []
    current_num = 0
    for i in nums:
        current_num += i
        new_nums.append(current_num)
    print(new_nums)



list_num = [3,1,2,10,1]
runningSum(list_num)
