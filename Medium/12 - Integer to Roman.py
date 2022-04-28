#https://leetcode.com/problems/integer-to-roman/submissions/

class Solution:
    conversion = {
            1: 'I',
            5: 'V',
            10: 'X',
            50:'L' ,
            100 : 'C',
            500 : 'D',
            1000: 'M',
        } 
    def digitToRoman(self, digit:int, primary:int, secondary:int):
        if digit == 0:
            return []
        elif digit < 4:
            return [self.conversion[secondary]*digit]
        elif digit == 4:
            return [self.conversion[secondary],self.conversion[primary]]
        elif digit < 9:
            return [self.conversion[primary],self.conversion[secondary]*(digit-5)]
        return [self.conversion[secondary],self.conversion[primary*2]]
        
    def intToRoman(self, num: int) -> str:       
        roman = []
        strNum = str(num)
        length = len(strNum)
        for i in strNum:
            if length == 4:
                roman.extend('M'*int(i))
            else:
                placeValue = 10**(length-1)
                roman.extend(
                    self.digitToRoman(int(i),
                    primary = 5*placeValue, 
                    secondary = placeValue,
                    )
                )
            length -= 1
            
        return ''.join(roman)
            
            
        