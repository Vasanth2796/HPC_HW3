class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt = {}
        length_max = 0
        st = 0
     
        for i in range(0, len(s)):          
            if s[i] in lt:
                st = max(st, lt[s[i]] + 1)
            # Updating the output as per the maximum value
            length_max = max(length_max, i-st + 1)
            lt[s[i]] = i # Updating the last index of present character. 
        return length_max
        
# User Input
s = "HighPerformanceComputing"
print("The input is", s)
a = Solution()
length = a.lengthOfLongestSubstring(s)
print("The length of the longest non-repeating character substring is", length)

# The time complexity for the code is O(n + d) where n is string input's length and d is number of characters in input string alphabet. 
 