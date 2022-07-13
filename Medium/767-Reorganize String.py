# https://leetcode.com/problems/reorganize-string/submissions/

class Solution:
    def reorganizeString(self, s: str) -> str:
        result = [None] * len(s)
        counts = Counter(s)
        minHeap = [(-count, char) for char, count in counts.items()]
        heapify(minHeap)

        lastItem = None
        for i in range(len(result)):
            reinsert = None
            count, char = heappop(minHeap)
            if lastItem is not None and char == lastItem:
                if len(minHeap) == 0:
                    return ''
                reinsert = (count, char)
                count, char = heappop(minHeap)

            result[i] = char
            lastItem = char
            count += 1
            if count < 0:
                heappush(minHeap, (count, char))
            if reinsert is not None:
                heappush(minHeap, reinsert)

        return ''.join(result)
