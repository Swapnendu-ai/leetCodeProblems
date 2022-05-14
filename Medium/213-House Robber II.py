# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        table = [[-1]*len(nums), [-1]*len(nums)]
        table[0][-1] = 0  # if we start from 0, we can't pick the last

        def robHelper(position, start):
            if table[start][position] != -1:
                return table[start][position]
            if position == len(nums)-1 and start != 0:
                table[start][position] = nums[position]
                return table[start][position]
            if position == len(nums)-2:
                table[start][position] = max(
                    robHelper(position+1, start),
                    nums[position]
                )
                return table[start][position]

            table[start][position] = max(
                robHelper(position+1, start),
                nums[position] + robHelper(position+2, start)
            )
            return table[start][position]

        return max(robHelper(0, 0), robHelper(1, 1))
