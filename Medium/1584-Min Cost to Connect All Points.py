# https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/

class Solution:
    def manhattan(self, point1, point2):
        return abs(point2[1]-point1[1])+abs(point2[0]-point1[0])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        point = points[0]
        seen = {tuple(point)}
        cost = 0
        while len(seen) < len(points):
            for nextPoint in points:
                nextPoint = tuple(nextPoint)
                if nextPoint not in seen:
                    heappush(pq, (self.manhattan(point, nextPoint), nextPoint))

            dst, point = heappop(pq)
            while point in seen:
                dst, point = heappop(pq)

            cost += dst
            seen.add(point)

        return cost
