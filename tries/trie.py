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

    def insert(self, word) -> None:
        curr = self.root

        for c in word:
            i = Trie.letterToChar(c)
            internal_node = curr.children[i]

            if not internal_node:
                internal_node = TrieNode(curr.val + c)
                curr.children[i] = internal_node

            curr = internal_node

        curr.is_entry = True

    def remove(self, word):
        self.removeHelper(self.root, word, 0)

    def removeHelper(self, node: TrieNode, word: str, index: int):
        if index == len(word):
            if not all(node.children):
                return True
            else:
                node.is_entry = False
                return False

        i = Trie.letterToChar(word[index])
        internal_node = node.children[i]

        if not internal_node:
            return False

        should_remove = self.removeHelper(internal_node, word, index+1)

        if should_remove:
            node.children[i] = None
            return True

        return False

    def search(self, word) -> bool:
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


def main():
    dict = Trie()

    dict.insert("cat")

    has_word = dict.search("cat")
    print(has_word)

    print(dict.startsWith("ca"))

    dict.remove("cat")

    has_word = dict.search("cat")
    print(has_word)


if __name__ == "__main__":
    main()
