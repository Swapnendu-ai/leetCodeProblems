# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        maxPrevHeight = 0
        maxPrevHeights = []

        for height in heights:
            maxPrevHeights.append(maxPrevHeight)
            maxPrevHeight = max(maxPrevHeight, height)

        maxNextHeight = 0
        maxNextHeights = []

        for i in range(len(heights)-1, -1, -1):
            maxNextHeights.append(maxNextHeight)
            maxNextHeight = max(maxNextHeight, heights[i])

        maxNextHeights.reverse()
        waterContent = map(
            lambda i: max(
                0, min(
                    maxNextHeights[i],
                    maxPrevHeights[i]
                ) - heights[i]),
            range(len(heights))
        )

        return sum(waterContent)

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
