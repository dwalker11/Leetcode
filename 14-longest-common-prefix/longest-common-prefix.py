class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        head, rest = strs[0], strs[1:]

        for i, c in enumerate(head):
            for str in rest:
                if i >= len(str) or str[i] != c:
                    return prefix
            prefix += c
    
        return prefix