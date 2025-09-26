def removeDuplicates(nums):
        k = 1 #First element is always unique, so we skip 0 and we go straight the 1 indexof the array
        for i in range(1, len(nums)):
            if (nums[i] != nums[k-1]):
                nums[k]=nums[i]
                k += 1
        return k

list_of_ints = [1,1,2]
removeDuplicates(list_of_ints)