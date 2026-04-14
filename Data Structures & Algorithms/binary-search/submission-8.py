class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left<=right:
            index = (right + left)//2
            value = nums[index]
            if value>target:
                right = index-1
            elif value<target:
                left = index+1
            else:
                return index

        return -1 
            

        