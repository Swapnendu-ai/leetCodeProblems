# https://leetcode.com/problems/reconstruct-itinerary/submissions/

class Solution:
    def findItineraryHelper(self, graph, src, count):
        if count == 0:
            return [src]
        # print(src,count)

        itinerary = None
        for idx in range(len(graph[src])):
            if not graph[src][idx][1]:
                graph[src][idx] = (graph[src][idx][0], True)
                itinerary = self.findItineraryHelper(
                    graph,
                    graph[src][idx][0],
                    count-1,
                )
                if itinerary is not None:
                    itinerary.append(src)
                    # print(itinerary,count)
                    return itinerary
                graph[src][idx] = (graph[src][idx][0], False)

        return itinerary

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for ticket in tickets:
            graph[ticket[0]].append((ticket[1], False))

        for src in graph:
            graph[src].sort()

        itinerary = self.findItineraryHelper(
            graph,
            'JFK',
            len(tickets),
        )
        itinerary.reverse()
        return itinerary
