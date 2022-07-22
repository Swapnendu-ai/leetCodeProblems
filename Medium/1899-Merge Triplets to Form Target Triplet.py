# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/submissions/

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = [False, False, False]

        for idx, triplet in enumerate(triplets):
            match[0] |= (
                triplet[0] == target[0] and
                triplet[1] <= target[1] and
                triplet[2] <= target[2]
            )
            match[1] |= (
                triplet[0] <= target[0] and
                triplet[1] == target[1] and
                triplet[2] <= target[2]
            )
            match[2] |= (
                triplet[0] <= target[0] and
                triplet[1] <= target[1] and
                triplet[2] == target[2]
            )

        return match[0] and match[1] and match[2]
