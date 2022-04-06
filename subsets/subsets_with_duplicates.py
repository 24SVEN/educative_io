def find_subsets(nums):
    subsets = []
    # TODO: Write your code here

    subsets.append([])
    for num in nums:
        for i in range(len(subsets)):
            temp = list(subsets[i])
            temp.append(num)
            if temp not in subsets:
                subsets.append(temp)

    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
