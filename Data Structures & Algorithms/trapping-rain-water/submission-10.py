class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]*len(height)
        right=[0]*len(height)

        maxValue = 0
        for i in range(len(height)):
            left[i] = maxValue
            maxValue = max(height[i], maxValue)
        
        maxValue = 0
        for i in range(len(height)-1, -1, -1):
            right[i] = maxValue
            maxValue = max(height[i], maxValue)
        
        total = 0
        for i in range(len(height)):
            value = min(left[i], right[i])-height[i]

            if value >0:
                total+=value
                
        return total
