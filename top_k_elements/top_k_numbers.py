import heapq


def find_k_largest_numbers(nums, k):
      result = []
      # TODO: Write your code here
      heapq.heapify(nums)

      for i in range(len(nums)-k):
            heapq.heappop(nums)

      return nums


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

