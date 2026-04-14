class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 1
        maxCount = 0
        nums.sort()

        print(nums)

        for index in range(len(nums)):
            if index==0:
                counter = 1
            else:
                if nums[index-1]+1 == nums[index]:
                    counter+=1
                elif nums[index-1] == nums[index]:
                    continue
                else:
                    counter = 1
            
            maxCount = max(maxCount, counter)
        
        return maxCount
