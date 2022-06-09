# https://leetcode.com/problems/combination-sum/submissions/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target <= 0:
            return []
        combinations = []
        for idx, can in enumerate(candidates):
            combWhenPicked = self.combinationSum(candidates[idx:], target-can)
            if len(combWhenPicked) > 0:
                for comb in combWhenPicked:
                    comb.append(can)
                combinations.extend(combWhenPicked)
            if can == target:
                combinations.append([can])

        return combinations
