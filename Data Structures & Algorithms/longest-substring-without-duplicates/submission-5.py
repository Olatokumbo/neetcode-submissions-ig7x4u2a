class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        total = 0
        seen = set()
        for right in range(len(s)):
            print(seen)
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            else:
                total = max(total, right-left+1)
                seen.add(s[right])
        return total

