# https://leetcode.com/problems/network-delay-time/submissions/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        for src, dest, time in times:
            graph[src][dest] = time

        pq = []
        seen = {k}
        timeTaken = [-1]*n
        timeTaken[k-1] = 0
        while len(seen) != n:
            for dst, time in graph[k].items():
                heappush(pq, (time+timeTaken[k-1], dst))

            if len(pq) == 0:
                return -1
            time, k = heappop(pq)
            while k in seen:
                if len(pq) == 0:
                    return -1
                time, k = heappop(pq)

            timeTaken[k-1] = time
            seen.add(k)

        return -1 if -1 in timeTaken else max(timeTaken)
