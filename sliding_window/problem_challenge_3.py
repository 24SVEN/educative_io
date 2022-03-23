
class Solution:
    def find_substring(self,str1, pattern):
        # TODO: Write your code here

        lw,rw = 0, 1

        h_map = {}
        for char in str1:
            if char in h_map:
                h_map[char] += 1
            else:
                h_map[char] = 1

        while lw<len(str1) and len(h_map) > 0:
            

        return ""
