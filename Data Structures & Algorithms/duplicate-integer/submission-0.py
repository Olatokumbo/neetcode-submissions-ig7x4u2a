class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for index, num in enumerate(nums):
            if num in my_map:
                return True
            else:
                my_map[num] = 1
        return False 