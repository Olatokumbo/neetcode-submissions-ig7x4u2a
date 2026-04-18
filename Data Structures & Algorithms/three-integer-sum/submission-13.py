class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # j=0
        res = []

        for j in range(len(nums)):
            if j != 0 and nums[j-1] == nums[j]:
                j+=1
            else:
                left = j+1
                right = len(nums)-1

                while left<right:
                    total = nums[j]+nums[left]+nums[right]
                    if total < 0:
                        left+=1
                    if total > 0:
                        right-=1
                    elif total == 0:
                        res.append([nums[j], nums[left], nums[right]])
                        left+=1
                        while nums[left-1] == nums[left] and left<right:
                            left+=1
        return res


            
        

