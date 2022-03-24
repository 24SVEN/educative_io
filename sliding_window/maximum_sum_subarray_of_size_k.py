#Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
class Solution:
    def max_sub_array_of_size_k(self,arr, k):
        # TODO: Write your code here
        lw,rw = 0,k-1
        max_sum = 0
        current_sum = sum(arr[0:k])
        while rw < len(arr)-1:
            rw+=1
            
            current_sum = current_sum+ arr[rw] - arr[lw]
            max_sum = max(max_sum, current_sum)
            lw+=1
        return max_sum


test = Solution()
print(test.max_sub_array_of_size_k([2, 1, 5, 1, 3, 2],3))
print(test.max_sub_array_of_size_k([2, 3, 4, 1, 5],2))