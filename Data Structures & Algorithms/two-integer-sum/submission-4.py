class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in my_map:
                return [my_map[diff], index]
            else:
                my_map[nums[index]] = index;