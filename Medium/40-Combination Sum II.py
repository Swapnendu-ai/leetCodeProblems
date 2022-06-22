# https://leetcode.com/problems/combination-sum-ii/submissions/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidateCount = list(Counter(candidates).items())

        def combinationSum2Helper(target, end=len(candidateCount)):
            if end == 0:
                return []
            candidate, count = candidateCount[end-1]
            targetCopy = target
            picked = []
            combinations = []
            while candidate <= targetCopy and count > 0:
                count -= 1
                picked.append(candidate)
                targetCopy -= candidate
                if targetCopy == 0:
                    combinations.append(picked)
                else:
                    combsWhenPicked = combinationSum2Helper(targetCopy, end-1)
                    for comb in combsWhenPicked:
                        comb.extend(picked)
                    combinations.extend(combsWhenPicked)
            combinations.extend(combinationSum2Helper(target, end-1))
            return combinations

        return combinationSum2Helper(target)
