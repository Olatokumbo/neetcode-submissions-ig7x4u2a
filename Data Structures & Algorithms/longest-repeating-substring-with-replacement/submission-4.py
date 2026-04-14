class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        res=0
        counter = {}
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0)+1

            while (right-left+1)-max(counter.values()) > k:
                counter[s[left]]-=1
                left+=1
            
            res = max(res, right-left+1)
        return res
