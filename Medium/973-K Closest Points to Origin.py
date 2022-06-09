# https://leetcode.com/problems/k-closest-points-to-origin/submissions/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        distanceToPointList = defaultdict(list)

        for point in points:
            dist = point[0]**2 + point[1]**2
            distanceToPointList[dist].append(point)
            heappush(heap, dist)

        results = []
        while k > 0:
            dist = heappop(heap)
            points = distanceToPointList[dist]
            results.extend(points[:k])
            k -= len(points)

        return results
