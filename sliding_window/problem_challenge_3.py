# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

class Solution:
    def find_substring(self,str1, pattern):
        # TODO: Write your code here

        lw,rw = 0,0

        h_map = {}
        for char in pattern:
            if char in h_map:
                h_map[char]+=1
            else:
                h_map[char]=1
        
        while lw<len(str1)-1:
            if str1[rw] in h_map:
                h_map[str1[rw]]-=1
                if h_map[str1[rw]] == 0:
                    del h_map[str1[rw]]
            rw+=1
            if len(h_map)==0:
                while lw<rw:
                    if str1[lw] not in h_map:
                        lw+=1
                    else:
                        return str1[lw:rw+1]


        return ""


test = Solution()
print(test.find_substring())