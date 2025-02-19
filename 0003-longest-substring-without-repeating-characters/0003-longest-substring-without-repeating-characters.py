class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        length = 0

        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char] >=left:
                left = seen[char] + 1
            else:
                length = max(length, right - left + 1)
            seen[char] = right
        
        return length
        
        