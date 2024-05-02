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
        

    def search(self, word: str) -> bool:
        i = 0
        curr = self.root
        while i != len(word):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
            i+=1
        return curr.last == True
        
    def startsWith(self, prefix: str) -> bool:
        i = 0
        curr = self.root
        while i != len(prefix):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
            i+=1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
