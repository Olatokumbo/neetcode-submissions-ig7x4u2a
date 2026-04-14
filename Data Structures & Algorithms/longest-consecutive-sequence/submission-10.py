class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxNum = 0
        nums = set(nums)

        for item in nums:
            if item-1 not in nums:
                length = 0
                while item+length in nums:
                    length+=1
                    maxNum = max(maxNum, length)
        
        return maxNum

