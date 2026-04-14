class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        total = 0

        maxValue = 0
        for index in range(len(height)):
            left[index] = maxValue
            maxValue = max(maxValue, height[index])
            
        maxValue = 0
        for index in range(len(height)-1, -1, -1):
            right[index] = maxValue
            maxValue = max(maxValue, height[index])

        for index in range(len(height)):
            value = min(left[index], right[index]) - height[index]
            if value > 0:
                total+=value

        return total

