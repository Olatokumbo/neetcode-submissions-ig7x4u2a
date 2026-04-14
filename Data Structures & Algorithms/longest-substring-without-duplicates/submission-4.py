class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total=0
        left=0
        seen=set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            total = max(total, right-left+1)
        return total
        


