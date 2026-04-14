class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 0

        while right < len(prices):
            if prices[left] <= prices[right]:
                profit = max(prices[right] - prices[left], profit)
                right+=1
            else:
                left = right
                right+=1

        return profit