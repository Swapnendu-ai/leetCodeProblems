# https://leetcode.com/problems/cheapest-flights-within-k-stops/submissions/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for srce, dest, price in flights:
            graph[srce][dest] = price

        orgVector = [float('infinity')]*n
        orgVector[src] = 0

        for step in range(k+1):
            #print(orgVector)
            newVector = orgVector.copy()
            for n1 in range(n):
                for n2, price in graph[n1].items():
                    newVector[n2] = min(newVector[n2], price+orgVector[n1])
            orgVector = newVector

        return -1 if orgVector[dst] == float('infinity') else orgVector[dst]
