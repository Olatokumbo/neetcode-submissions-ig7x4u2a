class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        min_compare = [0]*len(height)
        total = 0

        maxValue = 0
        for index in range(len(height)):
            prev = height[index-1]
            if index==0:
                prev=0
            maxValue = max(maxValue, prev)
            left[index] = maxValue
            
        maxValue = 0
        for index in range(len(height)-1, -1, -1):
            if index==len(height)-1:
                prev=0
            else:
                prev = height[index+1]
            maxValue = max(maxValue, prev)
            right[index] = maxValue

        print(left)
        print(right)

        for index in range(len(height)):
            value = min(left[index], right[index])
            min_compare[index] = value
        print(min_compare)

        for index in range(len(height)):
            value = min_compare[index] - height[index]
            if value>0:
                total+=value

        return total

