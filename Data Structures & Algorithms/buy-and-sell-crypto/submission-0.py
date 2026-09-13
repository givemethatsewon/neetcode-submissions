class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimum can be 0

        l = 0 # buy 날짜
        max_profit = 0
        # 제일 쌀 때 buy 제일 비쌀때 sell
        for r in range(1, len(prices)): # sell 날짜(창문)
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
        
        return max_profit




        
        