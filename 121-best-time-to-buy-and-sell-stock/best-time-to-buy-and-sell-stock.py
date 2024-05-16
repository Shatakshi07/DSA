class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        diff=0
        s=prices[0]
        while i<len(prices) :
            diff=max(diff, prices[i]-s)
            if s>prices[i]:
                s=prices[i]
            i+=1
        return diff