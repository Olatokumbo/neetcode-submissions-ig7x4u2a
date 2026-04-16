class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        total = 0

        maxNum = 0
        for index in range(1, len(height)):
            maxNum = max(maxNum, height[index-1])
            left[index] = maxNum

        maxNum = 0
        for index in range(len(height)-2, -1, -1):
            maxNum = max(maxNum, height[index+1])
            right[index] = maxNum

        for index in range(len(height)):
            value = min(left[index], right[index]) - height[index]
            if value < 0:
                total+=0
            else:
                total+=value
        
        return total