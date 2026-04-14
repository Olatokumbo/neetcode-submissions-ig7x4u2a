class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []

        valueMax = 0
        for index in range(len(height)):
            left.append(valueMax)
            valueMax = max(valueMax, height[index])
        
        valueMax = 0
        for index in range(len(height)-1, -1, -1):
            right.append(valueMax)
            valueMax = max(valueMax, height[index])

        right.reverse()
        total = 0
        for index in range(len(height)):
            value=min(left[index], right[index])-height[index]
            if value > 0:
                total+=value
        return total
