# https://leetcode.com/problems/add-strings/submissions/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        index = 1
        result = 0
        carry = 0
        while index <= min(len(num1),len(num2)):
            temp = carry + int(num1[-index]) + int(num2[-index])
            result += temp%10 * 10 ** (index-1)
            carry = temp//10
            index += 1

        while index <= len(num1):
            temp = carry + int(num1[-index])
            result += temp%10 * 10 ** (index-1)
            carry = temp//10
            index += 1

        while index <= len(num2):
            temp = carry + int(num2[-index])
            result += temp%10 * 10 ** (index-1)
            carry = temp//10
            index += 1

        if carry:
            result += carry * 10 ** (index-1)

        return str(result)
