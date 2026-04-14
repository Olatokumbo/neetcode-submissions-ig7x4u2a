class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = 0
        counter = 0
        nums.sort()

        for index in range(len(nums)):
            if index == 0:
                counter = 1

            else:
                if nums[index-1]+1 ==nums[index]:
                    counter+=1
                    total = max(total, counter)
                elif nums[index-1]==nums[index]:
                    continue
                else:
                    print(counter)
                    total = max(total, counter)
                    counter = 1
        return max(total, counter)