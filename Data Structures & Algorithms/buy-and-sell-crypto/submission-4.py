class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit=0
        smallestValue=prices[0]

        for item in range(1, len(prices)):
            if prices[item]<smallestValue:
                smallestValue = prices[item]
            mProfit = max(mProfit, prices[item] - smallestValue)
        return mProfit