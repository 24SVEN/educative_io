#Given a string, find the length of the longest substring in it with no more than K distinct characters.


# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
class Solution:
    def longest_substring_with_k_distinct(self,str1, k):
        # TODO: Write your code here

        h_map={}

        rw,lw = 0,0

        longest_substring = 0

        while rw<len(str1):
            if str1[rw] in h_map:
                h_map[str1[rw]] +=1
            else:
                h_map[str1[rw]] = 1
            

            if len(h_map) <= k:
                longest_substring = max(longest_substring,rw-lw+1)
            while len(h_map) >k and lw<rw:
                if str1[lw] in h_map:
                    h_map[str1[lw]] -= 1
                if h_map[str1[lw]] == 0:
                    del h_map[str1[lw]]
                lw+=1

            rw +=1

        return 0 if len(str1) == 0 else longest_substring

test = Solution()
print(test.longest_substring_with_k_distinct('araaci',2))
print(test.longest_substring_with_k_distinct('araaci',1))
print(test.longest_substring_with_k_distinct('cbbebi',3))
print(test.longest_substring_with_k_distinct('cbbebi',10))