def find_single_numbers(nums):
    # TODO: Write your code here
    #hash map method
    dict_sn = {}

    for i in range(len(nums)):
        if nums[i] in dict_sn:
            dict_sn[nums[i]] += 1
        else:
            dict_sn[nums[i]] = 1

    final_answer = []
    for key,val in dict_sn.items():
        if val == 1:
            final_answer.append(key)
    
    return final_answer


    #XOR method


def main():
    print('Single numbers are:' + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()
