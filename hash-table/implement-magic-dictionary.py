class MagicDictionary:

    def __init__(self):
        self.magic = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.magic.extend(dictionary)

    def search(self, searchWord: str) -> bool:
        for word in self.magic:
            if len(word) == len(searchWord) and word != searchWord:
                i = count = 0
                while i < len(word):
                    if word[i] != searchWord[i]:
                        count += 1
                    if count > 1:
                        break
                    i += 1
                if count == 1:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
