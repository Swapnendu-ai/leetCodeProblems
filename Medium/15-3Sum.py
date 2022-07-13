# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = defaultdict(lambda: defaultdict(set))

        def twoSum(nums, target, key):
            history = {}
            for num in nums:
                if num in history:
                    triplets[key][history[num]].add(num)
                history[target-num] = num

        for idx1, num1 in enumerate(nums):
            twoSum(nums[idx1+1:], -num1, num1)

        tripletList = []
        for num1 in triplets.keys():
            for num2 in triplets[num1].keys():
                for num3 in triplets[num1][num2]:
                    tripletList.append((num1, num2, num3))

        return tripletList
