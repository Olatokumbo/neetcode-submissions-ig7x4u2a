class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, value in enumerate(nums):
            if index !=0 and nums[index-1]==value:
                continue
            else:
                left, right = index+1, len(nums)-1
                while(left<right):
                    threeSum = nums[left]+nums[right]+value
                    if threeSum>0:
                        right-=1
                    elif threeSum<0:
                        left+=1
                    else:
                        res.append([value, nums[left], nums[right]])
                        left+=1
                        while nums[left]==nums[left-1] and left < right:
                            left+=1
        return res

