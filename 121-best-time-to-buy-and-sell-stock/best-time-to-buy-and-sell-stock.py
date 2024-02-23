class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left  = 0
        right = 1
        max_profit = 0 ## the logic is here. Even if we update the start and end the maximum profit is the one we are going to return 
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit) #it will update only if the data is more
            else:
                left = right
            right += 1
        return max_profit