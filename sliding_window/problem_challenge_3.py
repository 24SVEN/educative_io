# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

class Solution:
    def find_substring(self,str1, pattern):
        # TODO: Write your code here

        lw,rw = 0,0
        smallest_substring = str1
        h_map = {}

        #convert list to dictionary
        for char in pattern:
            if char not in h_map:
                h_map[char]= 1
            else:
                h_map[char] += 1
        
        while lw<len(str1)-1:
            if str1[rw] in h_map:
                h_map[str1[rw]] += 1

            
            if all([val >= 0 for val in h_map.values()]):
            
                while lw<rw and all([val >= 0 for val in h_map.values()]):
                    if len(smallest_substring) > len(str1[lw:rw+1]):
                        smallest_substring = str1[lw:rw+1]


                    if str1[lw] in h_map:
                        h_map[str1[lw]] -= 1
                        lw+=1
                    else:
                        h_map[str1[lw-1]]+=1


            rw+=1


        return smallest_substring


test = Solution()
print(test.find_substring('aabdec','abc'))