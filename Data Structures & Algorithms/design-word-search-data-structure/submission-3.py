class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()        

    def addWord(self, word: str) -> None:
        cur = self.head
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                l = word[i]
                if l == '.':
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False

                else: 
                    if l not in cur.children:
                        return False
                    
                    cur = cur.children[l]
            

            return cur.endOfWord

        return dfs(0,self.head)

