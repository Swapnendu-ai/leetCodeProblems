# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def isPalindrome(self, start, end: str) -> bool:
        if self.dpTable[start][end] is not None:
            return self.dpTable[start][end]

        if start+1 >= end -1:
            return self.s[start] == self.s[end]

        self.dpTable[start][end] = (self.s[start] == self.s[end]
                                         and self.isPalindrome(start+1, end-1))

        return self.dpTable[start][end]

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.dpTable = [[None for _ in s] for _ in s]
        maxString = s[0]
        for start in range(len(s)):
            self.dpTable[start][start] = True
            for end in range(start+len(maxString), len(s)):
                if s[start] == s[end] and self.isPalindrome(start, end):
                        maxString = s[start:end+1]
        return maxString



s = Solution()

print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("a"*1000))
print(s.longestPalindrome("wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"))
