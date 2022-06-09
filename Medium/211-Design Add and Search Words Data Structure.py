# https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        root = self.trie

        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]

        root[None] = None

    def search(self, word: str) -> bool:
        def searchHelper(root, word):
            if root is None:
                return False
            if len(word) == 0:
                return None in root
            if '.' == word[0]:
                for nextRoot in root.values():
                    found = searchHelper(nextRoot, word[1:])
                    if found:
                        return True
                return False
            if word[0] in root:
                return searchHelper(root[word[0]], word[1:])
            return False

        return searchHelper(self.trie, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
