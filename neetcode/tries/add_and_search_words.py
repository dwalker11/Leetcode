class Node:

    def __init__(self, val=""):
        self.is_entry = False
        self.val = val
        self.children = [None] * 26

    def letterToChar(char: str):
        return ord(char) - ord("a")


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            i = Node.letterToChar(c)
            internal_node = curr.children[i]

            if not internal_node:
                internal_node = Node(curr.val + c)
                curr.children[i] = internal_node

            curr = internal_node

        curr.is_entry = True

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word, 0)

    def searchHelper(self, node: Node, word: str, index: int) -> bool:
        if index == len(word):
            return node.is_entry

        c = word[index]

        if c != '.':
            i = Node.letterToChar(c)
            internal_node = node.children[i]

            if not internal_node:
                return False

            return self.searchHelper(internal_node, word, index+1)

        for child in node.children:
            if child and self.searchHelper(child, word, index+1):
                return True

        return False


dict = WordDictionary()

dict.addWord("bat")
dict.addWord("cat")
dict.addWord("cad")

words = ["cat", "ca.", ".at", "c."]

for word in words:
    result = "Yes" if dict.search(word) else "No"
    print(f"Does the dictonary have an entry for '{word}'? {result}")
