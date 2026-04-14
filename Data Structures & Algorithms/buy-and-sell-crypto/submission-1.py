class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        total = 0

        while right<len(prices):
            total = max(total, prices[right]-prices[left]) 
            if prices[right]<prices[left]:
                left = right 
            right+=1
        
        return total
