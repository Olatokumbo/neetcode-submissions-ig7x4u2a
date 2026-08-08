class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        left, right = 0, len(heights)-1

        while left<right:
            w = min(heights[left], heights[right])*(right-left)
            maxW = max(w, maxW)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1

        return maxW 
