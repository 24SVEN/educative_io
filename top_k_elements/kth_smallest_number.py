import heapq
def find_Kth_smallest_number(nums, k):
  # TODO: Write your code here
      return heapq.nsmallest(k,nums)[-1]
