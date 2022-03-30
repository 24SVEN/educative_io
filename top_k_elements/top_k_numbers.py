import heapq


def find_k_largest_numbers(nums, k):
      result = []
      # TODO: Write your code here
      heapq.heapify(nums)

      for i in range(k):
            heapq.heappush(result,nums[i])

      for i in range(k,len(nums)):
            if nums[i] > result[0]:
                  heapq.heappushpop(result,nums[i])

      return result


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

