class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        my_map = {}

        for right in range(len(s)):
            my_map[s[right]] = my_map.get(s[right], 0)+1
            while (right-left+1) - max(my_map.values()) > k:
                my_map[s[left]]-=1
                left+=1
            res = max(res, (right-left+1))
        return res