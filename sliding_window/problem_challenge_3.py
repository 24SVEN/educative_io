# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"


class Solution:
    def find_substring(self,str1, pattern):
        # TODO: Write your code here

        lw,rw = 0,0
        smallest_substring = str1 + 'L'
        h_map = {}

        #convert list to dictionary
        for char in pattern:
            if char not in h_map:
                h_map[char]= 1
            else:
                h_map[char] += 1
        
        #the substring needs to have all or more of the characters in hmap

        check_map = {}

        while rw < len(str1):

            #only add to the dictionary if it's a required character
            rw_char = str1[rw]
            if rw_char in h_map:
                if rw_char not in check_map:
                    check_map[rw_char]= 1
                else:
                    check_map[rw_char] += 1

            while self.check_if_valid(h_map,check_map):
                smallest_substring = smallest_substring if len(smallest_substring) < (rw-lw+1) else str1[lw:rw+1]
                if str1[lw] in check_map:
                    check_map[str1[lw]] -=1
                    if check_map[str1[lw]] == 0:
                        del check_map[str1[lw]] 

                lw +=1


            rw += 1


        return '' if smallest_substring == str1 + 'L' else smallest_substring

    def check_if_valid(self,dict_req,dict_check):
        #Lists should be the same amount
        if len(dict_req) != len(dict_check):
            return False
        
        #Check every key in the requirement and if all the values are equal or greater, function will pass True
        for key,val in dict_req.items():
            if dict_check[key] < val:
                return False

        return True


test = Solution()
print(test.find_substring('aabdec','abc'))   #abdec
print(test.find_substring('aabdec','abac'))  #aabdec
print(test.find_substring('abdbca','abc'))   #bca
print(test.find_substring('adcad','abc'))   #''