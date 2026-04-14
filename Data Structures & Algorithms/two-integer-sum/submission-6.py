class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if value in my_map:
                return [my_map[value], index]
            else:
                my_map[diff] = index