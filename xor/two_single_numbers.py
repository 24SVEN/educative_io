def find_single_numbers(nums):
    # TODO: Write your code here
    #hash map method
    # dict_sn = {}

    # for i in range(len(nums)):
    #     if nums[i] in dict_sn:
    #         dict_sn[nums[i]] += 1
    #     else:
    #         dict_sn[nums[i]] = 1

    # final_answer = []
    # for key,val in dict_sn.items():
    #     if val == 1:
    #         final_answer.append(key)
    
    # return final_answer


    #XOR method

    # decimal  | binary
    # 2            0010
    # ,1           0001
    # ,3           0011
    # ,2           0010
    # get the XOR of the all the numbers

    n1_xor_n2 = 0

    for num in nums:
        n1_xor_n2 ^= num

    #create rightmost bitmask
    mask = 1

    while mask & n1_xor_n2 != 0:
        mask = mask << 1

    num1, num2 = 0, 0

    for num in nums:
        t1=bin(num1)
        t2=bin(num2)
        if (num & mask) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]

#https://www.youtube.com/watch?v=dF4wL3BiYiA

    #print('Single numbers are:' + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

