from collections import deque
def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])

    for num in nums:
        for i in range(len(subsets)):
            temp = list(subsets[i])
            temp.append(num)
            subsets.append(temp)

    return subsets


def main():

  #print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
