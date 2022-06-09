# https://leetcode.com/problems/permutations-ii/submissions/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        numCount = Counter(nums)

        def permuteUniqueHelper(numCount) -> List[List[int]]:
            if len(numCount) == 1:
                return [list(numCount.keys())*list(numCount.values()).pop()]
            permutations = []
            for num, count in numCount.items():
                numCountDup = numCount.copy()
                if count > 1:
                    numCountDup[num] -= 1
                else:
                    del numCountDup[num]
                smallPerm = permuteUniqueHelper(numCountDup)
                for perm in smallPerm:
                    perm.append(num)

                permutations.extend(smallPerm)
            return permutations

        return permuteUniqueHelper(numCount)
