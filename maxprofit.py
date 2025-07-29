'''
Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.
Note: Stock must be bought before being sold.
'''
class Solution:
    def maximumProfit(self, prices):
        # code here
        n = len(prices)
        maxdif = 0
        '''for i in range(0,n-1):
            for j in range(i+1,n):
                dif = prices[j] - prices[i]
                if dif > maxdif:
                    maxdif = dif
        return maxdif
        '''
        min = prices[0]
        for i in range(1,n):
            if prices[i] < min:
                min = prices[i]
            dif = prices[i] - min
            if dif > maxdif:
                maxdif = dif
        return maxdif
