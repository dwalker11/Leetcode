def checkInculsion(s1: str, s2: str) -> bool:
    def getHash():
        x = {}
        for c in s1:
            x[c] = x.get(c, 0) + 1
        return x

    def incrementCount(h, k):
        x = h[k]
        h[k] = x + 1

    def decrementCount(h, k):
        x = h[k]
        h[k] = x - 1

    h = getHash()

    l = r = 0
    while r < len(s2):
        current = s2[r]
        count = h.get(current)

        if l == r and count is None:
            l += 1
            r = l
            continue

        if count is not None and count > 0:
            decrementCount(h, s2[r])
            r += 1
        else:
            incrementCount(h, s2[l])
            l += 1

        if len(s1) == len(s2[l:r]):
            return True

    return False


results = checkInculsion("ab", "eidboaoo")
print(f"Expected False got {results}")

results = checkInculsion("adc", "dcda")
print(f"Expected True got {results}")

results = checkInculsion("abc", "lecabee")
print(f"Expected True got {results}")

results = checkInculsion("abc", "lecaabee")
print(f"Expected False got {results}")
