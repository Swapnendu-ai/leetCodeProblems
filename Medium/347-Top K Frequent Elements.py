# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = sorted(Counter(nums).items(),
                        key=lambda x: x[1], reverse=True)[:k]
        return [x[0] for x in counts]
