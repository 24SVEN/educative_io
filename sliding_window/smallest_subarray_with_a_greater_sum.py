#Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
#leetcode 209

class Solution:
    def smallest_subarray_sum(self,s, arr):
    # TODO: Write your code here

        lw,total,rw = 0,0,0
        smallest_length = float('inf')

        for rw in range(len(arr)):
            rw += 1
            while total < s:
                total += arr[rw]
                
            
            smallest_length = min(smallest_length,rw-lw+1)
            total -= arr[lw]
            lw +=1




        return smallest_length


test = Solution()
print(test.smallest_subarray_sum(7,[2, 1, 5, 2, 3, 2]))
# print(test.smallest_subarray_sum(7,[2, 1, 5, 2, 8]))
# print(test.smallest_subarray_sum(8,[3, 4, 1, 1, 6]))