# https://leetcode.com/problems/subsets-ii/submissions/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        numCount = list(Counter(nums).items())

        def subsetsWithDupHelper(end=len(numCount)):
            if end <= 0:
                return [[]]
            num, count = numCount[end-1]
            subsetsWithoutNum = subsetsWithDupHelper(end-1)
            picked = []
            subsets = []
            for _ in range(count):
                picked.append(num)
                for subset in subsetsWithoutNum:
                    subset = subset.copy()
                    subset.extend(picked)
                    subsets.append(subset)
            subsets.extend(subsetsWithoutNum)
            return subsets

        return subsetsWithDupHelper()
