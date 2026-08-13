class TrieNode:
    def __init__(self):
        self.worddict = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.worddict:
                curr.worddict[c] = TrieNode()
            curr = curr.worddict[c] 
        curr.eow = True        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.worddict.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.worddict:
                        return False
                    curr = curr.worddict[c]

            return curr.eow

        return dfs(0, self.root)
