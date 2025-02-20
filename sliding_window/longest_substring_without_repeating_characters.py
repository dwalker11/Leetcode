def lengthOfLongestSubstring(s: str):
    results = 0
    seen = set()

    for i in range(0, len(s)):
        if s[i] in seen:
            break
        else:
            seen.add(s[i])

    start = 1
    results = len(seen)
    window = results + 1

    while window < len(s):
        found_longer_substring = searchSubString(s, start, window)

        if not found_longer_substring:
            break
        else:
            results = window
            window += 1

    return results


def searchSubString(s, start, window):
    def search():
        seen = set()

        for i in range(start, stop):
            if s[i] in seen:
                return False
            else:
                seen.add(s[i])

        return True

    stop = start + window
    while stop - 1 < len(s):
        if search():
            return True
        else:
            start += 1
            stop = start + window

    return False


results = lengthOfLongestSubstring(" ")
print(f"Expected 1 got {results}")

results = lengthOfLongestSubstring("dvdf")
print(f"Expected 3 got {results}")

results = lengthOfLongestSubstring("aab")
print(f"Expected 2 got {results}")

results = lengthOfLongestSubstring("pwwkew")
print(f"Expected 3 got {results}")

results = lengthOfLongestSubstring("xyzxyzxyz")
print(f"Expected 3 got {results}")
