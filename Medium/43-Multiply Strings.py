# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        layers = []
        maxPossibleResultLength = len(num1)+len(num2)+1
        num1List = [c for c in num1]
        num1List.reverse()
        for i, digit in enumerate(num1List):
            layer = [0]*i
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                prod = int(digit) * int(num2[j]) + carry
                carry = prod // 10
                layer.append(prod % 10)

            if carry > 0:
                layer.append(carry)
            layer.extend([0]*(maxPossibleResultLength-len(layer)))
            layers.append(layer)

        carry = 0
        result = []
        for index in range(len(layers[-1])):
            sumAtThisCol = carry
            for layer in layers:
                sumAtThisCol += layer[index]

            carry = sumAtThisCol // 10
            result.append(sumAtThisCol % 10)

        if carry > 0:
            result.append(carry)
        #print(result)
        firstNonZeroIndex = len(result)-1
        while result[firstNonZeroIndex] == 0:
            firstNonZeroIndex -= 1

        result = result[:firstNonZeroIndex+1]
        result.reverse()
        return ''.join([str(num) for num in result])
