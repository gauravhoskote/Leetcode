class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        i = 0
        while i!= len(word):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
            i+=1
        curr.last = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        curr = trie.root
        sol = ''
        while len(curr.children.keys()) == 1 and curr.last == False:
            for k,v in curr.children.items():
                sol = sol + k
                curr = curr.children[k]
        return sol
