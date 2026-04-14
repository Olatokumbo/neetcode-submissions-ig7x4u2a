class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for item in nums:
            if item in dups:
                return True
            else:
                dups[item] = True
        return False
