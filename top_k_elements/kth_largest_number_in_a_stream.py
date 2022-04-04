
#These are all getting timeout errors on leetcode. Need to review
#https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/
import heapq
class KthLargestNumberInStream:
    def __init__(self, nums, k):
        # TODO: Write your code here
        self.k = k
        self.num_list = nums

    def add(self, num):
        # TODO: Write your code here
        self.num_list.append(num)


        
        min_heap = []

        for i in range(self.k):
            heapq.heappush(min_heap,self.num_list[i])

        for i in range(self.k,len(self.num_list)):
            if min_heap[0] < self.num_list[i]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,self.num_list[i])


        return min_heap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()

