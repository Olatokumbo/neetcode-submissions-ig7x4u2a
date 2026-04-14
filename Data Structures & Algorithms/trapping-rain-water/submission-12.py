class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)

        res = 0

        maxValue = 0
        for i in range(len(height)):
            left[i] = maxValue
            maxValue = max(height[i], maxValue)

        maxValue = 0
        for i in range(len(height)-1, -1, -1):
            right[i] = maxValue
            maxValue = max(height[i], maxValue)

        for i in range(len(height)):
            minimum = min(left[i], right[i])
            total = minimum - height[i]

            if total > 0:
                res+=total
        
        return res