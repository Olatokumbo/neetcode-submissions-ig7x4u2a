class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in my_map.keys():
                return [my_map[diff], index]

            my_map[value] = index