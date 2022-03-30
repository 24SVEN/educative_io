
#Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. 
#It is given that all words are of the same length.

# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
class Solution:
    def find_word_concatenation(self,str1, words):
        result_indices = []
        # TODO: Write your code here

        dict_words = {}

        for word in words:
            dict_words[word] = 1 + dict_words.get(word,0)
        
        current_count = 0



        return result_indices


test = Solution()
print(test.find_word_concatenation('catfoxcat',["cat", "fox"]))