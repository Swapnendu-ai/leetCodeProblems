# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            flag = True
            while stack and flag:
                if temperatures[stack[-1]] > temperatures[i]:
                    output[i] = stack[-1]-i
                    flag = False
                else:
                    stack.pop()
            stack.append(i)

        return output
