# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countLetters(s: str) -> Dict[str, int]:
            count = {}
            for c in s:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
            return (count, s)

        letterCounts = map(countLetters, strs)
        anagramGroups = []

        for letterCount in letterCounts:
            newGroup = True
            for group in anagramGroups:
                if letterCount[0] == group[0][0]:
                    group.append(letterCount)
                    newGroup = False

            if newGroup:
                anagramGroups.append([letterCount])

        return [[elem[1] for elem in group] for group in anagramGroups]
