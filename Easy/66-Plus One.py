# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            sum = digits[i]+carry
            carry = sum // 10
            digits[i] = sum % 10
            if carry == 0:
                return digits

        if carry:
            return [carry] + digits
