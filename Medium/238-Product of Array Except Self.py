# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodWithout0 = None
        for num in nums:
            if num == 0:
                if prodWithout0 is None:
                    prodWithout0 = prod
                else:
                    prodWithout0 = 0
            else:
                if prodWithout0 is not None:
                    prodWithout0 *= num
            prod *= num

        return [prod//num if num != 0 else prodWithout0 for num in nums]
