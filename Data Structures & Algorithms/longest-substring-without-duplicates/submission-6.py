class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seen = set()
        left, right = 0, 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left]) 
                left+=1
            seen.add(s[right])
            right+=1
            maxLength = max(maxLength, right-left)

        return maxLength