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


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        current = candidates[-1]
        combinations = []
        targetCopy = target
        picked = []
        # print(candidates[:-1],target,current)
        while current <= targetCopy:
            targetCopy -= current
            picked.append(current)
            if targetCopy == 0:
                combinations.append(picked)
                # print(current,combinations)
            else:
                recursionResult = self.combinationSum(
                    candidates[:-1], targetCopy)
                for result in recursionResult:
                    result.extend(picked)
                    combinations.append(result)
                # print(combinations)
        combinations.extend(self.combinationSum(candidates[:-1], target))
        return combinations
