from collections import deque
def find_subsets(nums):
    
#https://www.youtube.com/watch?v=xFWgZ5DTjFo


    # subsets = []
    # # start by adding the empty subset
    # subsets.append([])

    # for num in nums:
    #     for i in range(len(subsets)):
    #         temp = list(subsets[i])
    #         temp.append(num)
    #         subsets.append(temp)

    # return subsets
    res = []

    for i in range(1<<(len(nums))):
        temp = []
        for j in range(len(nums)):
            print((i & (1<<j)),bin((i & (1<<j))))
            if (i & (1<<j)):
                temp.append(nums[j])
        res.append(temp)

    return res




def main():

  #print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
