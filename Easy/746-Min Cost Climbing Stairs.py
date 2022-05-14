# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [-1]*len(cost)

        def minCostClimbingStairsHelper(position):
            if minCost[position] != -1:
                return minCost[position]
            if position >= len(cost)-2:
                minCost[position] = cost[position]
                return minCost[position]

            minCost[position] = (
                cost[position] +
                min(
                    minCostClimbingStairsHelper(position+1),
                    minCostClimbingStairsHelper(position+2)
                )
            )
            return minCost[position]

        return min(minCostClimbingStairsHelper(0), minCostClimbingStairsHelper(1))
