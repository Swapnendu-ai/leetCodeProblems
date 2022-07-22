# https://leetcode.com/problems/coin-change-2/submissions/

class Solution:
    def changeHelper(self, amount, coins, end, table):
        if amount == 0:
            return 1  
        if end == 0:
            return 0      
        if amount in table[end-1]:
            return table[end-1][amount]
        
        pick = coins[end-1]
        numberOfCombinations = 0
        if pick <= amount:
            numberOfCombinations = self.changeHelper(amount - pick,coins,end,table)
                
          
        numberOfCombinations +=  self.changeHelper(amount,coins,end-1,table)
        table[end-1][amount] = numberOfCombinations
        # print(amount,end, numberOfCombinations)
        return numberOfCombinations
        
            
    def change(self, amount: int, coins: List[int]) -> int:
        table = [{} for _ in coins]
        
        return self.changeHelper(amount,coins,len(coins),table)