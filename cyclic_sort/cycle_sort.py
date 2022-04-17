def cyclic_sort(nums):
    # TODO: Write your code here
    
    lw = 0
    rw = len(nums)-1

    while lw < rw:
        if nums[lw] > nums[lw+1]:
            nums[lw],nums[lw+1] = nums[lw+1],nums[lw]
            lw = 0
        else:
            lw += 1
    return nums

print(cyclic_sort([3, 1, 5, 4, 2]))