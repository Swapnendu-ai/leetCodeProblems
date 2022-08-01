# https://leetcode.com/problems/palindrome-partitioning/submissions/

class Solution:
    def isPalindrome(self,s,start,end):
        if start == end:
            return True
        
        while end-start > 1: 
            if s[start]!= s[end]:
                return False
            start+=1
            end -= 1
        
        return s[start] == s[end]
    
    def partitionH(self, s, table, start):
        if start == len(s)-1:
            return [[s[-1]]]
        
        table[start] = []
        for end in range(start,len(s)-1):
            if self.isPalindrome(s,start,end):
                if end < len(s)-1 and table[end+1] is None:
                    table[end+1] = self.partitionH(s,table,end+1)
                    
                for partitions in table[end+1]:
                    table[start].append([s[start:end+1]] + partitions)
        
        if self.isPalindrome(s,start,len(s)-1):
            table[start].append([s[start:]])
        return table[start]
    
    def partition(self, s: str) -> List[List[str]]:
        table = [None]*len(s)
        return self.partitionH(s,table,0)