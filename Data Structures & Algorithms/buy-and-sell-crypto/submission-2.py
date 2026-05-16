class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left, right = 0, len(prices) - 1
        buy, sell = left, right

        while buy < sell and left < len(prices) and right >= 0:
            if prices[left] < prices[buy]:
                if left < sell:
                    buy = left
            if prices[right] > prices[sell]:
                if right > buy:
                    sell = right
            left+=1
            right-=1
        profit = prices[sell] - prices[buy]
        if profit < 0:
            return 0
        return profit


        