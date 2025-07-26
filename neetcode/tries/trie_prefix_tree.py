class TrieNode:

    def __init__(self, val=""):
        self.val = val
        self.is_entry = False
        self.children = [None for _ in range(26)]


class Trie:

    def letterToChar(char: str):
        return ord(char) - ord("a")

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            i = Trie.letterToChar(c)
            internal_node = curr.children[i]

            if not internal_node:
                internal_node = TrieNode(curr.val + c)
                curr.children[i] = internal_node

            curr = internal_node

        curr.is_entry = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            i = Trie.letterToChar(c)
            internal_node = curr.children[i]

            if not internal_node:
                return False

            curr = internal_node

        return curr.is_entry

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            i = Trie.letterToChar(c)
            internal_node = curr.children[i]

            if not internal_node:
                return False

            curr = internal_node

        return True
