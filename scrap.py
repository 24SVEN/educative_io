class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        count_r = 0
        count_l = 0
        for i in range(len(s)):
            if s[i] == 'R':
                count_r += 1
            elif s[i] == 'L':
                count_l += 1
            
            if count_l == count_r:
                count += 1
                count_r = 0
                count_l = 0
        return count

test = Solution()
print(test.balancedStringSplit('RLRRLLRLRL')) #4
print(test.balancedStringSplit('RL')) #1
print(test.balancedStringSplit('RRR')) #0